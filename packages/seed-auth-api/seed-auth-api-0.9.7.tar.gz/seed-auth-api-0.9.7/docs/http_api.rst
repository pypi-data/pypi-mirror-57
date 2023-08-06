.. _http-api:


Seed Auth HTTP API
==================

.. _authentication:

Authentication
^^^^^^^^^^^^^^
Authentication is done via token authentication.The tokens endpoint can be
used to create a token. The token can then be placed in the header for
requests to the other endpoints.

**Example request**:

.. sourcecode:: http

   POST /endpoint/ HTTP/1.1
   Content-Type: application/json
   Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b


.. _permissions:

Permissions
^^^^^^^^^^^

While you can store any string as a permission, there are a few permissions
that have specific meaning within the Seed Auth API.

Create permissions are not linked to specific instances, whereas admin, read,
and write permissions are.

A user automatically has read/write permissions for themselves.

All users have read permissions for all users and organizations.

All members of an organization have read access to that organization's teams.

Permissions can be assigned either to a user or a team. All users can add and
remove permissions for all teams and users, except for the following
permissions, which can only be set be set by a person with org:admin
permission.


org:admin
    Can create/read/write/delete users, and teams that are part of the
    organization, and can add users to the organization that they are an admin
    for. Can read/write the organization that they are admin for.
team:admin
    Can modify the team they have permission for, and add and remove existing
    users to that team.

.. http:get:: /user/

   Get the user details, and list of permissions that a user currently has
   access to, for the user authorized by the given token.

   :>header Authorization: "Token " followed by the token to verify
   :status 200: The token is valid.
   :status 401: The token is invalid/missing.

   **Example request**:

   .. sourcecode:: http

      GET /user/ HTTP/1.1
      Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b


   **Example response**:

   .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "id": "1",
        "url": "https://example.org/users/1/",
        "first_name": "Jon",
        "last_name": "Snow",
        "email": "jonsnow@castleblack.net",
        "admin": false,
        "active": true,
        "permissions": [
            {
                "id": "2",
                "type": "org:admins",
                "object_id": "3",
                "namespace": "__auth__"
            },
            {
                "id": "5",
                "type": "foo:bar:baz",
                "object_id": "7",
                "namespace": "foo_app"
            }
        ]
    }

**Permission structure**:

Each permission is an object containing the following fields.

id
    The unique ID for the permission
type
    The string representing the type of permission.
object_id
    A string that uniquely identifies the object that this permission acts
    upon. null if this permission does not act on a specific object.
namespace
    A string used to namespace a set of permissions for a specific app, to
    avoid "type" collisions.

.. _pagination:

Pagination
^^^^^^^^^^

When the results set is larger than a configured amount, the data is broken up
into pages.

You can navigate to specific pages using the 'page' parameter. Links to the
next and previous page (if available) will be provided in the 'Link' header.

Example:

.. sourcecode:: http

   GET /endpoint/ HTTP/1.1
   Authorization: token .....


   HTTP/1.1 200 OK
   Content-Type: application/json
   Link: <https://example.com/endpoint/?page=2>; rel="next"

   [....]

.. _tokens:

Tokens
^^^^^^

For the token endpoints, no authentication is required.

.. http:post:: /user/tokens/

   Create a new token for the provided user. This will invalidate all other
   tokens for that user.

   :<json str email: The username of the user to create the token for.
   :<json str password: The password of the user to create the token for.
   :>json str token: The generated token.
   :status 201: When the token is successfully generated.
   :status 401: When the user credentials are incorrect.
   :status 403: When the user is inactive.

   **Example request**:

   .. sourcecode:: http

      POST /user/tokens/ HTTP/1.1
      Content-Type: application/json

      {
        "email": "testuser@example.org",
        "password": "testpassword"
      }


   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json

      {
        "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
      }



Password resets
^^^^^^^^^^^^^^^

.. ATTENTION::
    This endpoint has not yet been implemented.

For the password reset endpoints, no authentication is required.

To reset a user's password, the following steps should be followed:

1. Make a request to the reset endpoint.
   This will make an HTTP request to the preconfigured endpoint with the user's
   details, and a token.
2. Make a request to the confirm endpoint, with the provided token and the new
   password.

.. http:post:: /passwords/resets/

   Start the process for resetting a user's password.

   :<json str email: The email of the user to reset the password for.
   :<json str app:
        The application that the token should go to, configured in settings.
        This value is optional, defaults to the default configured application.
   :code 202:
        The password reset process was started, or the username doesn't exist.
        The same code is returned for both as to not leak user information

   **Example request**:

   .. sourcecode:: http

      POST /passwords/resets/ HTTP/1.1
      Content-Type: application/json

      {"email":"jonsnow@castleblack.org","app":"numi"}

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 202 Accepted

.. http:post:: /passwords/confirmations/

   Reset the users password using the provided token.

   :<json str token: The provided token.
   :<json str password: The new password.
   :code 204: The password was successfully reset.
   :code 401: The token was incorrect.

   **Example request**:

   .. sourcecode:: http

      POST /password/confirmations/ HTTP/1.1
      Content-Type: application/json

      {"password":"gh0st","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvbiBTbm93In0.H7huFJ_ioqf1-_qzZQ6VLHOJpnqhdDiZFV2VdkIt7LY"}

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content


Organizations
^^^^^^^^^^^^^

Organizations provide a grouping of users, although users do not have to belong
to an organization, and they can also belong to many organizations. Teams have
to belong to exactly one organization, but an organization can have many teams.

.. http:post:: /organizations/

    Creates a new organization.

    Requires admin user.

    :<json str title: The title of the organization.
    :>json str title: The title of the created organization.
    :>json str id: The id of the created organization.
    :>json list teams: The list of teams that the organization has.
    :>json list users: The list of users that are part of the organization.
    :>json str url: The URL for this organization.
    :>json bool archived: True if the organization has been archived.
    :status 201: When the organization is successfully generated.
    :status 400: When there is invalid information to create the organization.

    **Example request**:

    .. sourcecode:: http

       POST /organizations/ HTTP/1.1
       Content-Type: application/json

       {
        "title": "Nights Watch"
       }


    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 201 Created
        Content-Type: application/json

        {
            "title": "Nights Watch",
            "id": "4",
            "teams": [],
            "url": "https://example.org/organizations/4/",
            "users": [],
            "archived": false
        }

.. _organizations-list:
.. http:get:: /organizations/

    Get a list of existing organizations

    Requires any user.

    :queryparam archived:
        (optional) If true, shows archived organizations. If false, shows
        organizations that are not archived. If both, shows all organizations.
        Defaults to false.

    **Example request**:

    .. sourcecode:: http

       GET /organizations/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       [
        {
            "title":"Nights Watch",
            "id":4,
            "teams":[],
            "url":"https://example.org/organizations/4/",
            "users":[],
            "archived": false
        },
        {
            "title":"Brotherhood Without Banners",
            "id":5,
            "teams":[],
            "url":"https://example.org/organizations/5/",
            "users":[],
            "archived": false
        }
       ]

.. http:get:: /organizations/(int:organization_id)/

    Get the details of an organization.

    Requires any user.

    :>json str title: The title of the created organization.
    :>json str id: The id of the created organization.
    :>json list teams: The list of teams that the organization has.
    :>json list users: The list of users that are a part of the organization.
    :>json str url: The URL for this organization.
    :>json bool archived: True if the organization has been archived.

    **Example request**:

    .. sourcecode:: http

       GET /organizations/4/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
        "title":"Night's Watch",
        "id":4,
        "teams":[],
        "url":"https://example.org/organizations/4/",
        "users":[],
        "archived": false
       }

.. _organizations-update:
.. http:put:: /organizations/(int:organization_id)/

    Update an existing organization.

    Requires admin user, or any user that has 'org:admin' permission for the
    specific organization.

    :<json str title: The title of the organization.
    :<json str archived: True if the organization is to be archived.
    :>json str id: The id of the created organization.
    :>json list teams: The list of teams that the organization has.
    :>json list users: The list of users that are part of the organization.
    :>json str url: The URL for this organization.
    :>json bool archived: True if the organization has been archived.

    :status 200: When the organization is successfully generated.
    :status 400: When there is invalid information to update the organization.

    **Example request**:

    .. sourcecode:: http

       PUT /organizations/4/ HTTP/1.1
       Content-Type: application/json

       {
        "title": "Brotherhood Without Banners",
        "archived": false
       }

    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
        "title":"Brotherhood Without Banners",
        "id":4,
        "teams":[],
        "url":"https://example.org/organizations/4/",
        "users":[],
        "archived": false
       }

.. http:delete:: /organizations/(int:organization_id)/

    Archive an organization. The organization will by default no longer be
    shown when :ref:`listing organizations <organizations-list>`, the
    organization's teams will by default no longer be shown when :ref:`listing
    teams <teams-list>`, and any permissions associated with the organization's
    teams will no longer take effect when checking whether a user has
    permission to perform an action.

    Archiving can be reversed by setting ``archived`` to ``true`` when
    :ref:`updating <organizations-update>` an organization.

    Requires admin user, or any user that has 'org:admin' for this
    organization.

    :status 204: Organization successfully archived

   **Example request**:

   .. sourcecode:: http

      DELETE /organizations/4/ HTTP/1.1

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 204 No Content

.. http:put:: /organizations/(int:organization_id)/users/(int:user_id)/

    Add a user to an existing organization.

    Requires admin user, or any user that has 'org:admin' permissions for that
    organization.

    :status 204: User was successfully added.

    **Example request**:

    .. sourcecode:: http

        PUT /organizations/4/users/2/ HTTP/1.1
        Content-Type: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content

.. http:delete:: /organizations/(int:organization_id)/users/(int:user_id)/

    Remove a user from an organization.

    Requires admin user, or any user that has 'org:admin' permission for that
    organization.

    :status 204: User was successfully removed from an organization

    **Example request**:

    .. sourcecode:: http

        DELETE /organizations/4/users/2/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content

.. http:post:: /organizations/(int:organization_id)/teams/

    Create a new team for an organization

    Only admin users, and users with org:admin permissions for the org may
    create teams.

    :<json str title: The title of the team.
    :<json bool archived: True if the team is archived.

    :>json str id: The ID of the created team.
    :>json str url: The URL of the created team.
    :>json str title: the title of the team.
    :>json list users: The list of users that belong to this team.
    :>json obj organization: The summary of the organization that the team belongs to.
    :>json list permissions: The permission list for the team.
    :>json bool archived: True if the team is archived.
    :status 201: Successfully created team.
    :status 400: Missing required information to create team.

    **Example request**:

    .. sourcecode:: http

        POST /organizations/7/teams/ HTTP/1.1
        Content-Type: application/json

        {
            "title": "Lord Commanders",
            "archived": false
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 201 Created
        Content-Type: application/json

        {
            "id": "2",
            "title": "Lord Commanders",
            "users": [],
            "permissions": [],
            "url": "https://example.org/teams/2/",
            "organization": {
                "url": "https://example.com/organizations/7/",
                "id": "7"
            },
            "archived": false
        }

.. http:get:: /organizations/(int:organization_id)/teams/

    See `Get list of teams`_. Limited to teams that belong to the organization.

.. http:get:: /organizations/(int:organization_id)/teams/(int:team:id)/

    See `Get team details`_. Limited to teams that belong to the organization.

.. http:put:: /organizations/(int:organization_id)/teams/(int:team:id)/

    See `Update team details`_. Limited to teams that belong to the organization.

.. http:delete:: /organizations/(int:organization_id)/teams/(int:team:id)/

    See `Archive team`_. Limited to teams that belong to the organization.

.. http:post:: /organizations/(int:organization_id)/teams/(int:team:id)/permissions/

    See `Add permission to team`_. Limited to teams that belong to the organization.

.. http:delete:: /organizations/(int:organization_id)/teams/(int:team:id)/permissions/(int:permission_id)/

    See `Remove permission from team`_. Limited to teams that belong to the organization.

.. http:put:: /organizations/(int:organization_id)/teams/(int:team:id)/users/(int:user_id)/

    See `Add user to team`_. Limited to teams that belong to the organization.

.. http:delete:: /organizations/(int:organization_id)/teams/(int:team:id)/user/(int:user_id)/

    See `Remove user from team`_. Limited to teams that belong to the organization.

Teams
^^^^^

.. _Get list of teams:
.. _teams-list:
.. http:get:: /teams/

    Get a list of all the teams you have read access to.

    admin users have read access to all teams. users with org:admin for an
    organization have read access to that organization's teams. users with
    team:admin permissions for a team have read access to that team. users
    that are part of the team, or part of the team's organization, have read
    access to that team.

    **Example request**:

    .. sourcecode:: http

        GET /teams/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK

        [
            {
                "id": "4",
                "title": "admins",
                "permissions": [],
                "users": [],
                "url": "https://example.org/teams/4/",
                "organization": {
                    "url": "https://example.org/organizations/7/",
                    "id": "7"
                },
                "archived": false
            }
        ]

.. http:get:: /teams/

    Allows filtering of teams to retreive a subset.

    :query string type_contains:
        The type field on one of the resulting team's permissions must contain
        this string. (optional)
    :query string object_id:
        All the object_id fields on one of the resulting team's permissions
        must equal this string. (optional)
    :quert string namespace:
        All the namespace fields on one of the resulting team's permissions
        must equal this string. (optional)

    **Example request**:

    .. sourcecode:: http

        GET /teams/?permission_contains=org&object_id=3&namespace=__auth__ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "4",
                "title": "organization admins",
                "users": [],
                "permissions":
                    [
                        {
                            "id": "2",
                            "type": "org:admin",
                            "object_id": "3",
                            "namespace": "__auth__"
                        }
                    ],
                "url": "https://example.org/teams/4/",
                "organization": {
                    "url": "https://example.org/organizations/3/",
                    "id": "3"
                },
                "archived": false
            },
            {
                "id": "7",
                "title": "other organization admins",
                "users": [],
                "permissions":
                    [
                        {
                            "id": "3",
                            "type": "org:admin",
                            "object_id": "3",
                            "namespace": "__auth__"
                        },
                        {
                            "id": "4",
                            "type": "foo:bar",
                            "object_id": "",
                            "namespace": "foo_app"
                        }
                    ],
                "url": "https://exmple.org/teams/6/",
                "organization": {
                    "url": "https://example.org/organizations/3/",
                    "id": "3"
                },
                "archived": false
            }
        ]


.. _Get team details:
.. http:get:: /teams/(int:team_id)/

    Get the details of a team.

    admin users have read access to all teams. users with org:admin for an
    organization have read access to that organization's teams. users with
    team:admin permissions for a team have read access to that team. users
    that are part of the team, or part of the team's organization, have read
    access to that team.

    :>json str id: the ID of the team.
    :>json str url: the URL of the team.
    :>json str title: the title of the team.
    :>json list users: The list of users that belong to this team.
    :>json obj organization: An object representing the organization that the team belongs to.
    :>json list permissions: The permission list for the team.
    :>json bool archived: True if team is archived.
    :status 200: Successfully retrieved team.

    **Example request**:

    .. sourcecode:: http

        GET /teams/2/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "id": "2",
            "title": "Lord Commanders",
            "permissions": [],
            "users": [],
            "url": "https://example.org/teams/2/",
            "organization": {
                "url": "https://example.org/organizations/7/",
                "id": "7"
            },
            "archived": false
        }

.. _Update team details:
.. _teams-update:
.. http:put:: /teams/(int:team_id)/

    Update the details of a team.

    Admin users can update teams. Users with org:admin permissions for a
    team's organization can update teams. Users with team:admin can modify
    the team that they are admin for.

    :<json str title: The title of the team.
    :<json bool archived: True if the team is archived.

    :>json str id: the id of the updated team.
    :>json str url: The URL of the updated team.
    :>json str title: the title of the team.
    :>json list users: The list of users that belong to this team.
    :>json obj organization: The summary of the organization that the team belongs to.
    :>json list permissions: The permission list for the team.
    :>json bool archived: True if the team is archived.
    :status 200: successfully updated team.

    **Example request**:

    .. sourcecode:: http

        PUT /teams/2/ HTTP/1.1
        Content-Type: application/json

        {
            "title": "Brotherhood without banners",
            "archived": false
        }

    **Example reponse**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "id": "2",
            "title": "Brotherhood without banners",
            "permissions": [],
            "users": [],
            "url": "https://example.org/teams/2/",
            "organization": {
                "url": "https://example.org/organizations/7/",
                "id": "7"
            },
            "archived": false
        }

.. _Archive team:
.. http:delete:: /teams/(int:team_id)/

    Archive a team. The team will by default no longer be shown when
    :ref:`listing teams <teams-list>`, and any permissions associated with the
    team will no longer take effect when checking whether a user has permission
    to perform an action.

    Archiving can be reversed by setting ``archived`` to ``true`` when
    :ref:`updating <teams-update>` a team.

    Admin users can archive teams. Users with org:admin permissions for a
    team's organization can archive teams. Users with team:admin can archive
    the team that they are admin for.

    :status 204: Team successfully archived.

    **Example request**:

    .. sourcecode:: http

        DELETE /teams/2/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content

.. _Add permission to team:
.. http:post:: /teams/(int:team_id)/permissions/

    Add a permission to a team.

    Any user that can see the team, can add permissions to that team.

    If the permission to be added is of type team:admin, then the user must
    have team:admin for the team specified by object_id, or org:admin for the
    team's organization, with the team specified by the object_id.

    If the permission to be added is of type org:admin, then the user must
    have org:admin for the organization specified by object_id.

    admin users can add any permissions.

    :<json str type: The string representing the permission.
    :<json str object_id:
        The id of the object that the permission acts on. null if it
        doesn't act on any object.
    :<json str namespace:
        The namespace for the permission, to avoid "type" collisions between
        apps.

    :>json str id: the id of the permission.
    :>json str type: the type of the permission.
    :>json str object_id: the object id that the permission acts on.
    :status 200: successfully added permission to the team.

    **Example request**:

    .. sourcecode:: http

        POST /teams/2/permissions/ HTTP/1.1
        Content-Type: application/json

        {
            "type": "org:admin",
            "object_id": "2",
            "namespace": "__auth__"
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "id": "17",
            "type": "org:admin",
            "object_id": "2",
            "namespace": "__auth__"
        }

.. _Remove permission from team:
.. http:delete:: /teams/(int:team_id)/permissions/(int:permission_id)/

    Remove a permission from a team.

    Any user that can see the team, can remove permissions from that team.
    
    If the permission to be removed is of type team:admin, then the user must
    have team:admin for the team specified by object_id, or org:admin for the
    team's organization, with the team specified by the object_id.

    If the permission to be removed is of type org:admin, then the user must
    have org:admin for the organization specified by object_id.

    admin users can remove any permission.

    :status 204: successfully removed permission from the team.

    **Example request**:

    .. sourcecode:: http

        DELETE /teams/2/permissions/17/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content

.. _Add user to team:
.. http:put:: /teams/(int:team_id)/users/(int:user_id)/

    Add an existing user to an existing team.

    :status 204: successfully added the user to the team.

    **Example request**:

    .. sourcecode:: http

        PUT /teams/2/users/1/ HTTP/1.1
        Content-Type: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content

.. _Remove user from team:
.. http:delete:: /teams/(int:team_id)/users/1/

    Remove a user from a team.

    :status 204: successfully removed the user from the team.

    **Example request**:

    .. sourcecode:: http

        DELETE /teams/2/users/1/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 OK

Users
^^^^^

.. http:get:: /users/

    Get a list of all users.

    Requires any authenticated user.

    **Example request**:

    .. sourcecode:: http

        GET /users/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "1",
                "url": "https://example.org/users/1/",
                "first_name": "Jon",
                "last_name": "Snow",
                "email": "jonsnow@castleblack.net",
                "admin": false,
                "active": true,
                "teams": [
                    {
                        "id": "2",
                        "url": "https://example.org/teams/2/"
                    }
                ],
                "organizations": [
                    {
                        "id": "4",
                        "url": "https://example.org/organizations/4/"
                    }
                ]
            }
        ]

.. http:post:: /users/

    Create a new user.

    Only admin users, and users with org:admin permissions can create new
    users. Only admin users are allowed to create other admin users.

    :<json str first_name: The (optional) first name of the user.
    :<json str last_name: The (optional) last name of the user.
    :<json str email: The email address of the user.
    :<json str password: The password for the user.
    :<json bool admin:
        (optional) True if the user is an admin user. Defaults to False.
    :<json bool active:
        (optional) False if the user is inactive. Inactive users cannot have
        tokens created, and permissions are also inactive. They do not show
        up in any users listing. Defaults to True.

    :>json str id: The ID for the user.
    :>json str url: The URL for the user.
    :>json str first_name: The (optional) first name of the user.
    :>json str last_name: The (optional) last name of the user.
    :>json str email: The email address of the user.
    :>json bool admin: True if the user is an admin user.
    :>json bool active: True if the user is active.
    :>json list teams: A list of all the teams a user is a member of.
    :>json list organizations:
        A list of all the organizations the user is a member of.

    :status 201: Successfully created user.

    **Example request**:

    .. sourcecode:: http

        POST /users/ HTTP/1.1
        Content-Type: application/json

        {
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jonsnow@castleblack.net",
            "password": "gh0st",
            "admin": false
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 201 Created
        Content-Type: application/json

        {
            "id": "1",
            "url": "https://example.org/users/1/",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jonsnow@castleblack.net",
            "admin": false,
            "active": true,
            "teams": [],
            "organizations": []
        }

.. http:get:: /users/(int:user_id)/

    Get details on a specific user.

    Requires an authenticated user.

    :>json str id: The ID for the user.
    :>json str url: The URL for the user.
    :>json str first_name: The (optional) first name of the user.
    :>json str last_name: The (optional) last name of the user.
    :>json str email: The email address of the user.
    :>json bool admin: True if the user is an admin user.
    :>json bool active: True if the user is active.
    :>json list teams: A list of all the teams a user is a member of.
    :>json list organizations:
        A list of all the organizations the user is a member of.

    **Example request**:

    .. sourcecode:: http

        GET /users/1/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "id": "1",
            "url": "https://example.org/users/1/",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jonsnow@castleblack.net",
            "admin": false,
            "active": true,
            "teams": [
                {
                    "id": "2",
                    "url": "https://example.org/teams/2/"
                }
            ],
            "organizations": [
                {
                    "id": "4",
                    "url": "https://example.org/organizations/4/"
                }
            ]
        }

.. http:put:: /users/(int:user_id)/

    Update the information of an existing user.

    Only the user themself, or a user with org:admin, or an admin user can
    update the user information. Only admin users can change a user to be an
    admin user.

    :<json str first_name: The (optional) first name of the user.
    :<json str last_name: The (optional) last name of the user.
    :<json str email: The email address of the user.
    :<json str password: The password for the user.
    :<json bool admin: (optional) True if the user is an admin user.
    :<json bool active: (optional) True if the user is active.

    :>json str id: The ID for the user.
    :>json str url: The URL for the user.
    :>json str first_name: The (optional) first name of the user.
    :>json str last_name: The (optional) last name of the user.
    :>json str email: The email address of the user.
    :>json bool admin: True if the user is an admin user.
    :>json bool active: True if the user is active.
    :>json list teams: A list of all the teams a user is a member of.
    :>json list organizations:
        A list of all the organizations the user is a member of.

    :status 200: Successfully updated user.

    **Example request**:

    .. sourcecode:: http

        PUT /users/1/ HTTP/1.1
        Content-Type: application/json

        {
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jonsnow@castleblack.org",
            "password": "gh0st",
            "admin": true
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 201 Created
        Content-Type: application/json

        {
            "id": "1",
            "url": "https://example.org/users/1/",
            "first_name": "Jon",
            "last_name": "Snow",
            "email": "jonsnow@castleblack.org",
            "admin": true,
            "active": true,
            "teams": [],
            "organizations": []
        }

.. http:delete:: /users/(int:user_id)/

    Remove an existing user. Sets the user to inactive instead of deleting
    the user.

    Only the user themself, or a user with org:admin, or an admin user can
    deactivate a user.

    User can be reactivated by setting active to true in
    :ref:`updating users <users-update>`.

    :status 204: Successfully deleted the user.

    **Example request**:

    .. sourcecode:: http

        DELETE /users/1/ HTTP/1.1

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 204 No Content
