from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from authapi.serializers import PermissionSerializer
from authapi.models import SeedTeam, SeedOrganization
from authapi.tests.base import AuthAPITestCase


class UserPermissionsTests(AuthAPITestCase):
    def test_get_empty_permissions(self):
        '''If the user isn't part of any teams that grant permissions, it
        should return the user information with an empty permission list.'''
        user = User.objects.create_user(
            username='foo@bar.org', email='foo@bar.org', password='password')
        token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get-user-permissions'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(user.id))
        self.assertEqual(response.data['email'], 'foo@bar.org')
        self.assertEqual(response.data['permissions'], [])

    def test_get_permissions_from_teams(self):
        '''If the user is part of teams that have permissions, those
        permissions should be granted to the user. The permissions on teams
        that the user is not a member of should not be given to the user.'''
        org = SeedOrganization.objects.create()
        teams = []
        for i in range(3):
            team = SeedTeam.objects.create(organization=org)
            team.permissions.create(
                type='foo%d' % i, namespace='bar%d' % i, object_id='%d' % i)
            teams.append(team)

        user = User.objects.create_user('foo@bar.org', password='password')
        token = Token.objects.create(user=user)
        teams[0].users.add(user)
        teams[1].users.add(user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('get-user-permissions')
        response = self.client.get(url)

        permissions = sorted(
            response.data['permissions'], key=lambda p: p['id'])
        context = self.get_context(url)
        expected_permissions = sorted(PermissionSerializer(
            instance=[teams[0].permissions.get(), teams[1].permissions.get()],
            many=True, context=context).data, key=lambda p: p['id'])
        self.assertEqual(permissions, expected_permissions)

    def test_get_permissions_from_archived_teams(self):
        '''Archived teams should not give users any permissions.'''
        org = SeedOrganization.objects.create()
        team = SeedTeam.objects.create(organization=org, archived=True)
        team.permissions.create(type='foo', namespace='bar', object_id='1')

        user = User.objects.create_user('foo@bar.org', password='password')
        token = Token.objects.create(user=user)
        team.users.add(user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get-user-permissions'))

        self.assertEqual(response.data['permissions'], [])

    def test_get_permissions_from_archived_organizations(self):
        '''Teams of archived organizations should not give users any
        permissions.'''
        org = SeedOrganization.objects.create(archived=True)
        team = SeedTeam.objects.create(organization=org)
        team.permissions.create(type='foo', namespace='bar', object_id='1')

        user = User.objects.create_user('foo@bar.org', password='password')
        token = Token.objects.create(user=user)
        team.users.add(user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get-user-permissions'))

        self.assertEqual(response.data['permissions'], [])

    def test_get_permissions_from_inactive_users(self):
        '''Inactive users should not have any permissions.'''
        org = SeedOrganization.objects.create()
        team = SeedTeam.objects.create(organization=org)
        team.permissions.create(type='foo', namespace='bar', object_id='1')

        user = User.objects.create_user(
            'foo@bar.org', password='password', is_active=False)
        token = Token.objects.create(user=user)
        team.users.add(user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get-user-permissions'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_permssions_from_unauthorized_users(self):
        '''If there is no token in the authentication error, we should return
        an unauthorized response.'''
        response = self.client.get(reverse('get-user-permissions'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
