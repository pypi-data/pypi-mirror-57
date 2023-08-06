import json
import responses

from django.conf import settings
from django.urls import reverse
from django.test import TestCase, Client, override_settings

from ..views import get_identity_addresses


class ViewTestsTemplate(TestCase):
    def setUp(self):
        self.client = Client()

    def login(self):
        self.client.login(username='testuser', password='testpass')
        session = self.client.session
        session['user_token'] = 'temptoken'
        session['user_permissions'] = [{"object_id": 1, "type": "ci:view"}]
        session['user_dashboards'] = []
        session['user_id'] = 123
        session['user_list'] = {'123': "fred@something.com"}
        session.save()

    def set_session_user_tokens(self):
        session = self.client.session
        session['user_tokens'] = {
            "SEED_IDENTITY_SERVICE": {
                "url": 'http://idstore.example.com/', "token": 'idstoretoken'},
            "HUB": {
                "url": 'http://hub.example.com/', "token": 'hubtoken'},
            "SEED_STAGE_BASED_MESSAGING": {
                "url": 'http://sbm.example.com/', "token": 'sbmtoken'},
            "SEED_MESSAGE_SENDER": {
                "url": 'http://ms.example.com/', 'token': 'mstoken'
            }
        }
        session.save()

    def add_identities_callback(self, num=10, identities=None, qs=None):
        """
        Adds a callback for getting the list of identities.

        If identities is specified, overwrites the auto generated identities
        specified by num.

        If qs is specified, ensures that the call contains the specified
        querystring.
        """
        url = 'http://idstore.example.com/identities/'
        if qs is not None:
            url = '{}search/{}'.format(url, qs)

        if identities is None:
            identities = [
                {
                    'identity': 'identity-{}'.format(i),
                    'details': {
                        'addresses': {
                            'msisdn': {
                                '+27{:0>9}'.format(i): {}
                            }
                        }
                    },
                    'created_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                    'updated_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                } for i in range(num)]

        data = {
            'results': identities,
        }

        responses.add(
            responses.GET, url, json=data, status=200,
            content_type='application/json', match_querystring=bool(qs))

    def add_identity_callback(self, identity='operator_id', details=None):
        if details is None:
            details = {
                'personnel_code': 'personnel_code',
                'facility_name': 'facility_name',
                'default_addr_type': 'msisdn',
                'receiver_role': 'role',
                'state': 'state',
                'addresses': {
                    'msisdn': {
                        '+2340000000000': {}
                    }
                }
            }

        responses.add(
            responses.GET,
            'http://idstore.example.com/identities/{}/'.format(identity),
            json={
                'identity': identity,
                'details': details,
                'created_at': '2016-01-01T10:30:21.0Z',
                'updated_at': '2016-01-01T10:30:21.0Z',
            },
            status=200,
            content_type='application/json')

    def add_registrations_callback(self, num=10, registrations=None, qs=None):
        if registrations is None:
            registrations = [
                {
                    'id': 'registration-{}'.format(i),
                    'reg_type': settings.STAGES[0][0],
                    settings.IDENTITY_FIELD: 'identity-{}'.format(i),
                    'validated': True,
                    'data': {},
                    'created_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                    'updated_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                }
                for i in range(num)
            ]

        url = 'http://hub.example.com/registrations/'
        if qs is not None:
            url = '{}{}'.format(url, qs)

        responses.add(
            responses.GET, url, match_querystring=bool(qs), status=200,
            json={
                'results': registrations,
            },
            content_type='application/json')

    def add_changes_callback(self, num=10, changes=None, qs=None):
        if changes is None:
            changes = [
                {
                    'id': 'change-{}'.format(i),
                    'action': settings.ACTIONS[0][0],
                    settings.IDENTITY_FIELD: 'identity-{}'.format(i),
                    'data': {},
                    'validated': True,
                    'created_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                    'updated_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                }
                for i in range(num)
            ]

        url = 'http://hub.example.com/changes/'

        if qs is not None:
            url = '{}{}'.format(url, qs)

        responses.add(
            responses.GET, url, status=200, match_querystring=bool(qs),
            json={
                'results': changes,
            },
            content_type='application/json')

    def add_subscriptions_callback(self, num=10, subscriptions=None, qs=None):
        if subscriptions is None:
            subscriptions = [
                {
                    'id': 'subscription-{}'.format(i),
                    'identity': 'identity-{}'.format(i),
                    'messageset': 1,
                    'next_sequence_number': i,
                    'language': 'zul_ZA',
                    'active': True,
                    'completed': False,
                    'created_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                    'updated_at': '2016-01-01T10:30:21.{:0>5}Z'.format(i),
                }
                for i in range(num)
            ]

        url = 'http://sbm.example.com/subscriptions/'

        if qs is not None:
            url = '{}{}'.format(url, qs)

        responses.add(
            responses.GET, url, status=200, match_querystring=bool(qs),
            json={
                'results': subscriptions,
            },
            content_type='application/json')

    def add_messagesets_callback(self, results=[]):
        responses.add(
            responses.GET,
            'http://sbm.example.com/messageset/',
            json={
                'results': results,
            },
            status=200,
            content_type='application/json')

    def add_auditlog_create_callback(self):
        responses.add(
            responses.POST,
            'http://localhost:8003/api/v1/auditlog/',
            json={"foo": "bar"},
            status=201,
            content_type='application/json'
        )

    def add_auditlog_callback(self, identity_id, num=3, auditlogs=None):
        if auditlogs is None:
            auditlogs = [
                {
                    'id': i,
                    "identity_id": identity_id,
                    "subscription_id": "12121212-afaa-43de-acb1-09f61ad4de99",
                    "action_at": "2016-08-03T19:39:26.464102Z",
                    "action_by": 123,
                    "action": "u",
                    "action_name": "Update",
                    "model": "subscription",
                    "detail": "Language changed from eng_ZA to afr_ZA"
                }
                for i in range(num)
            ]

        url = 'http://localhost:8003/api/v1/auditlog/?identity_id={}'.format(
            identity_id)

        responses.add(
            responses.GET, url, status=200, match_querystring=True,
            json={
                'results': auditlogs,
            },
            content_type='application/json')


@override_settings(IDENTITY_MESSAGES_PAGE_SIZE=100)
class ViewTests(ViewTestsTemplate):
    def add_messageset_language_callback(self):
        responses.add(
            responses.GET,
            'http://sbm.example.com/messageset_languages/',
            json={
                "2": ["afr_ZA", "eng_ZA"],
                "4": ["afr_ZA", "eng_ZA", "zul_ZA"]
            },
            status=200,
            content_type='application/json')

    def test_redirect_to_login(self):
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please login to see this page")

    def test_get_identy_addresses_good(self):
        self.assertEqual(get_identity_addresses({
            'details': {
                'default_addr_type': 'msisdn',
                'addresses': {
                    'msisdn': {
                        '1234567890': {},
                    }
                }
            }
        }), {'1234567890': {}})

    def test_get_identy_addresses_bad(self):
        self.assertEqual(get_identity_addresses({}), {})
        self.assertEqual(get_identity_addresses({
            'details': {
                'default_addr_type': 'msisdn'
            }
        }), {})
        self.assertEqual(get_identity_addresses({
            'details': {
                'default_addr_type': 'foo',
                'addresses': {
                    'msisdn': {
                        '1234567890': {},
                    }
                }
            }
        }), {})

    @responses.activate
    @override_settings(IDENTITY_FIELD='mother_id')
    def test_change_subscription(self):
        self.login()
        self.set_session_user_tokens()
        self.add_auditlog_create_callback()

        subscription_id = "sub12312-63e2-4acc-9b94-26663b9bc267"
        identity_id = "mother01-63e2-4acc-9b94-26663b9bc267"

        self.add_messagesets_callback(results=[
            {"id": 2, "short_name": "test"},
            {"id": 4, "short_name": "test2"}
        ])
        self.add_messageset_language_callback()

        responses.add(
            responses.POST,
            'http://hub.example.com/change_admin/',
            json={
                "mother_id": identity_id,
                "subscription": subscription_id
            },
            status=201,
            content_type='application/json'
        )
        responses.add(
            responses.GET,
            "http://sbm.example.com/subscriptions/%s/" % subscription_id,
            match_querystring=True,
            json={
                "id": subscription_id,
                "identity": identity_id,
                "active": True,
                "completed": False,
                "lang": "eng_ZA",
                "messageset": 2,
                "next_sequence_number": 32,
                "schedule": 132,
                "process_status": 0,
                "version": 1,
                "metadata": {},
                "created_at": "2015-07-10T06:13:29.693272Z",
                "updated_at": "2015-07-10T06:13:29.693272Z"
            },
            status=200,
            content_type='application/json')

        response = self.client.post(
            "/subscriptions/%s/" % subscription_id,
            {
                "language": "zul_ZA",
                "messageset": 4
            })

        self.assertEqual(response.status_code, 200)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Successfully added change.')

        change_request = responses.calls[2].request
        self.assertEqual(change_request.url,
                         "http://hub.example.com/change_admin/")
        self.assertEqual(
            json.loads(change_request.body),
            {
                "mother_id": identity_id,
                "messageset": "test2",
                "language": "zul_ZA",
                "subscription": subscription_id
            })

        audit_request_language = responses.calls[3].request
        self.assertEqual(
            json.loads(audit_request_language.body),
            {
                "identity_id": identity_id,
                "action": "Update",
                "action_by": 123,
                "model": "subscription",
                "detail": "Updated language: eng_ZA to zul_ZA"
            })

        audit_request_messageset = responses.calls[4].request
        self.assertEqual(
            json.loads(audit_request_messageset.body),
            {
                "identity_id": identity_id,
                "action": "Update",
                "action_by": 123,
                "model": "subscription",
                "detail": "Updated messageset: test to test2"
            })

    @responses.activate
    @override_settings(METRIC_API_URL='http://metrics-api.org/')
    def test_dashboard_metric(self):
        """
        When requesting a dashboard widget the metric api must be called and
        data must be returned in the correct format
        """
        self.login()
        self.set_session_user_tokens()

        responses.add(
            responses.GET,
            "http://metrics-api.org/metrics/?start=-30d&interval=1d&"
            "m=one.total.sum&m=two.total.sum&m=three.total.sum&nulls=zeroize",
            match_querystring=True,
            json={
                'one.total.sum': [{'y': 1.0, 'x': 111}, {'y': 2.0, 'x': 222}],
                'two.total.sum': [{'y': 4.0, 'x': 333}, {'y': 5.0, 'x': 444}],
                'three.total.sum': [{'y': 6.0, 'x': 123}, {'y': 7.0, 'x': 321}]
            },
            status=200,
            content_type='application/json'
        )

        response = self.client.get(
            "/api/v1/metric/?start=-30d&interval=1d&m=one.total.sum&m="
            "two.total.sum&m=three.total.sum&nulls=zeroize",
            follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf-8')), {
            "objects": [{
                    "values": [{"y": 1.0, "x": 111}, {"y": 2.0, "x": 222}],
                    "key": "one.total.sum"
                }, {
                    "values": [{"y": 4.0, "x": 333}, {"y": 5.0, "x": 444}],
                    "key": "two.total.sum"
                }, {
                    "values": [{"y": 6.0, "x": 123}, {"y": 7.0, "x": 321}],
                    "key": "three.total.sum"
                }
            ]})


class IdentityViewTest(ViewTestsTemplate):
    def add_message_sender_inbound_responses(
            self, count=1, identity='operator_id'):
        message = {
            'content': 'Inbound message',
            'created_at': '2017-09-12T00:00Z',
            'updated_at': '2017-09-12T00:00Z',
        }

        responses.add(
            responses.GET,
            ('http://ms.example.com/inbound/?from_identity={}'
             '&ordering=-created_at'.format(identity)),
            match_querystring=True,
            json={'results': [message for i in range(count)]},
            status=200,
            content_type='application/json')

    def add_message_sender_outbound_responses(
            self, count=1, identity='operator_id'):
        message = {
            'content': 'Outbound message',
            'created_at': '2017-09-12T00:00Z',
            'updated_at': '2017-09-12T00:00Z',
        }

        responses.add(
            responses.GET,
            ('http://ms.example.com/outbound/?to_identity={}'
             '&ordering=-created_at'.format(identity)),
            match_querystring=True,
            json={'results': [message for i in range(count)]},
            status=200,
            content_type='application/json')

    def setUp(self):
        self.login()
        self.set_session_user_tokens()
        self.add_messagesets_callback([{
            'id': 1,
            'short_name': 'ms.1',
            'default_schedule': 2,
        }])
        self.add_identity_callback()
        self.add_registrations_callback(
            num=0, qs='?{}=operator_id'.format(settings.IDENTITY_FIELD))
        self.add_changes_callback(
            num=0, qs='?{}=operator_id'.format(settings.IDENTITY_FIELD))
        self.add_subscriptions_callback()

    @responses.activate
    def test_should_display_outbound_messages(self):
        self.add_message_sender_inbound_responses()
        self.add_message_sender_outbound_responses()
        self.add_auditlog_callback("operator_id")
        response = self.client.get('/identities/operator_id/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Outbound message')

    @responses.activate
    @override_settings(IDENTITY_MESSAGES_PAGE_SIZE=1)
    def test_should_paginate_outbound_messages(self):
        self.add_message_sender_inbound_responses()
        self.add_message_sender_outbound_responses(count=2)
        self.add_auditlog_callback("operator_id")
        response = self.client.get('/identities/operator_id/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '?outbound_page=2')

    @responses.activate
    def test_should_display_inbound_messages(self):
        self.add_message_sender_inbound_responses()
        self.add_message_sender_outbound_responses()
        self.add_auditlog_callback("operator_id")
        response = self.client.get('/identities/operator_id/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inbound message')

    @responses.activate
    @override_settings(IDENTITY_MESSAGES_PAGE_SIZE=1)
    def test_should_paginate_inbound_messages(self):
        self.add_message_sender_inbound_responses(count=2)
        self.add_message_sender_outbound_responses()
        self.add_auditlog_callback("operator_id")
        response = self.client.get('/identities/operator_id/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '?inbound_page=2')

    @responses.activate
    def test_optout_identity(self):
        self.add_message_sender_inbound_responses()
        self.add_message_sender_outbound_responses()
        self.add_auditlog_create_callback()
        self.add_auditlog_callback('operator_id')
        subscription = {
            'lang': 'eng_NG',
            'created_at': '2016-11-22T08:12:45.343829Z',
            'messageset': 4,
            'schedule': 5,
            'url': 'url',
            'completed': False,
            'initial_sequence_number': 1,
            'updated_at': '2016-11-22T08:12:52.411545Z',
            'version': 1,
            'next_sequence_number': 1,
            'process_status': 0,
            'active': True,
            'id': '10176584-2a47-42b6-b9f3-a3a98070f35e',
            'identity': '17cf37cf-edd6-4634-88e3-f793575f7e3a',
            'metadata': {
                'scheduler_schedule_id':
                    'a64d153f-1515-42c1-997a-9a3444c916fc'
            }
        }

        responses.add(
            responses.GET,
            'http://sbm.example.com/subscriptions/?identity=operator_id',
            match_querystring=True,
            json={
                'next': None,
                'results': [subscription],
            },
            status=200,
            content_type='application/json')

        responses.add(
            responses.POST,
            'http://idstore.example.com/optout/',
            json={
                "identity": "operator_id",
                "optout_type": "stop",
                "address_type": "msisdn",
                "address": "+2340000000000",
                "request_source": "ci"},
            status=200,
            content_type='application/json')

        responses.add(
            responses.POST,
            'http://hub.example.com/optout_admin/',
            json={"mother_id": "operator_id"},
            status=201,
            content_type='application/json'
        )

        response = self.client.post(
            "/identities/operator_id/",
            {"optout_identity": ['']})

        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(messages[0].message, 'Successfully opted out.')

        [_, _, request_audit] = filter(
            lambda r: r.method == 'POST',
            (r.request for r in responses.calls))

        self.assertEqual(json.loads(request_audit.body), {
            "identity_id": "operator_id",
            "action": "Update",
            "action_by": 123,
            "model": "identity",
            "detail": "Optout identity"
        })

    @responses.activate
    def test_add_subscription_to_identity(self):
        """
        A POST request to the identities endpoint for adding a subscription
        should return a success message, and POST the correct data to the
        stage based messaging application to create the new subscription.
        """
        self.add_identity_callback(
            'identity_id', {'preferred_language': "zul_ZA"})
        self.add_message_sender_outbound_responses(identity='identity_id')
        self.add_message_sender_inbound_responses(identity='identity_id')
        self.add_registrations_callback(qs="?mother_id=identity_id")
        self.add_changes_callback(qs="?mother_id=identity_id")
        self.add_auditlog_create_callback()
        self.add_auditlog_callback('identity_id')

        responses.add(
            responses.POST,
            'http://sbm.example.com/subscriptions/',
            json={}, status=201, content_type='application/json'
        )

        response = self.client.post(
            reverse('identities-detail', kwargs={'identity': 'identity_id'}),
            {'add_subscription': '', 'messageset': 1}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context['messages'])[0].message,
            "Successfully created a subscription.")
        [request, request_audit] = filter(
            lambda r: r.method == 'POST',
            (r.request for r in responses.calls))
        self.assertEqual(json.loads(request.body), {
            'active': True,
            'completed': False,
            'identity': 'identity_id',
            'lang': 'zul_ZA',
            'messageset': 1,
            'next_sequence_number': 1,
            'process_status': 0,
            'schedule': 2,
        })

        self.assertEqual(json.loads(request_audit.body), {
            "identity_id": "identity_id",
            "action": "Create",
            "action_by": 123,
            "model": "subscription"
        })

    @responses.activate
    @override_settings(LANGUAGE_FIELD='lang')
    def test_add_subscription_to_identity_language_field(self):
        """
        If there is a custom language field set in the django settings, then
        that field should determine what the language should be for the new
        subscription.
        """
        self.add_identity_callback(
            'identity_id', {'lang': "zul_ZA"})
        self.add_message_sender_outbound_responses(identity='identity_id')
        self.add_message_sender_inbound_responses(identity='identity_id')
        self.add_registrations_callback(qs="?mother_id=identity_id")
        self.add_changes_callback(qs="?mother_id=identity_id")
        self.add_auditlog_create_callback()
        self.add_auditlog_callback('identity_id')

        responses.add(
            responses.POST,
            'http://sbm.example.com/subscriptions/',
            json={}, status=201, content_type='application/json'
        )

        response = self.client.post(
            reverse('identities-detail', kwargs={'identity': 'identity_id'}),
            {'add_subscription': '', 'messageset': 1}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context['messages'])[0].message,
            "Successfully created a subscription.")
        [request, request_audit] = filter(
            lambda r: r.method == 'POST',
            (r.request for r in responses.calls))
        self.assertEqual(json.loads(request.body), {
            'active': True,
            'completed': False,
            'identity': 'identity_id',
            'lang': 'zul_ZA',
            'messageset': 1,
            'next_sequence_number': 1,
            'process_status': 0,
            'schedule': 2,
        })

        self.assertEqual(json.loads(request_audit.body), {
            "identity_id": "identity_id",
            "action": "Create",
            "action_by": 123,
            "model": "subscription"
        })

    @responses.activate
    def test_deactivate_subscription(self):
        """
        A POST request to the identities endpoint for deactivating a
        subscription should return a success message, and POST the correct data
        to the stage based messaging application to deactivate the
        subscription.
        """
        self.add_identity_callback(
            'identity_id', {'preferred_language': "zul_ZA"})
        self.add_message_sender_outbound_responses(identity='identity_id')
        self.add_message_sender_inbound_responses(identity='identity_id')
        self.add_registrations_callback(qs="?mother_id=identity_id")
        self.add_changes_callback(qs="?mother_id=identity_id")
        self.add_auditlog_create_callback()
        self.add_auditlog_callback('identity_id')

        responses.add(
            responses.PATCH,
            'http://sbm.example.com/subscriptions/subscription_id/',
            json={}, status=201, content_type='application/json'
        )

        response = self.client.post(
            reverse('identities-detail', kwargs={'identity': 'identity_id'}),
            {
                'deactivate_subscription': '',
                'subscription_id': "subscription_id"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context['messages'])[0].message,
            "Successfully deactivated the subscription.")

        [request, request_audit] = filter(
            lambda r: r.method in ('POST', 'PATCH'),
            (r.request for r in responses.calls))

        self.assertEqual(json.loads(request.body), {'active': False})
        self.assertEqual(json.loads(request_audit.body), {
            "identity_id": "identity_id",
            "subscription_id": "subscription_id",
            "action": "Update",
            "action_by": 123,
            "model": "subscription",
            "detail": "Deactivated subscription"
        })


class IdentitiesViewTest(ViewTestsTemplate):
    @override_settings(IDENTITY_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_identity_list(self):
        """
        Doing a plain GET request should return a page worth of identities.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_identities_callback(num=10)

        response = self.client.get(reverse('identities'))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['identities']), 5)

    @override_settings(IDENTITY_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_filtered_identity_list_error(self):
        """
        If the data submitted for filtering the list of identities is invalid,
        then the errors should be sent in the form, as well as an empty list
        of identities.
        """
        self.login()
        self.set_session_user_tokens()

        qs = "?address_value=1234&address_type=invalid"
        response = self.client.get('{}{}'.format(reverse('identities'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['identities']), 0)
        self.assertFalse(context['form'].is_valid())
        self.assertEqual(len(context['form'].errors), 1)

    @override_settings(IDENTITY_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_filtered_identity_list(self):
        """
        If there are query parameters for filtering the list of identities,
        then that list should be filtered.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_identities_callback(
            num=10, qs='?details__addresses__msisdn=1234')

        qs = "?address_value=1234&address_type=msisdn"
        response = self.client.get('{}{}'.format(reverse('identities'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['identities']), 5)


class RegistrationsViewTest(ViewTestsTemplate):
    @override_settings(REGISTRATION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_registration_list(self):
        """
        Doing a GET request should return a page of registrations.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_registrations_callback(num=10)

        response = self.client.get(reverse('registrations'))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['registrations']), 5)

    @override_settings(REGISTRATION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_registration_list_filter_error(self):
        """
        If the data submitted for filtering the list of registrations is
        invalid, then the errors should be sent in the form, as well as an
        empty list of registrations.
        """
        self.login()
        self.set_session_user_tokens()

        qs = "?mother_id=&stage=invalid&validated="
        response = self.client.get('{}{}'.format(reverse('registrations'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['registrations']), 0)
        self.assertFalse(context['form'].is_valid())
        self.assertEqual(len(context['form'].errors), 1)

    @override_settings(REGISTRATION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_filtered_registrations_list(self):
        """
        If there are query parameters for filtering the list of registrations,
        then that list should be filtered.
        """
        self.login()
        self.set_session_user_tokens()
        qs = "?validated=True&{}=1234&{}={}".format(
            settings.IDENTITY_FIELD, settings.STAGE_FIELD,
            settings.STAGES[0][0])
        self.add_registrations_callback(num=10, qs=qs)

        qs = "?mother_id=1234&stage={}&validated=True".format(
            settings.STAGES[0][0])
        response = self.client.get('{}{}'.format(reverse('registrations'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['registrations']), 5)


class ChangesViewTest(ViewTestsTemplate):
    @override_settings(CHANGE_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_changes_list(self):
        """
        Doing a GET request should return a page of changes.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_changes_callback(num=10)

        response = self.client.get(reverse('changes'))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['changes']), 5)

    @override_settings(CHANGE_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_changes_list_filter_error(self):
        """
        If the data submitted for filtering the list of changes is invalid,
        then the errors should be sent in the form, as well as an empty list
        of changes.
        """
        self.login()
        self.set_session_user_tokens()

        qs = "?mother_id=&action=invalid&validated="
        response = self.client.get('{}{}'.format(reverse('changes'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['changes']), 0)
        self.assertFalse(context['form'].is_valid())
        self.assertEqual(len(context['form'].errors), 1)

    @override_settings(CHANGE_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_filtered_changes_list(self):
        """
        If there are query parameters for filtering the list of changes, then
        that list should be filtered.
        """
        self.login()
        self.set_session_user_tokens()
        qs = "?validated=True&{}=1234&action={}".format(
            settings.IDENTITY_FIELD, settings.ACTIONS[0][0])
        self.add_changes_callback(num=10, qs=qs)

        qs = "?mother_id=1234&action={}&validated=True".format(
            settings.ACTIONS[0][0])
        response = self.client.get('{}{}'.format(reverse('changes'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['changes']), 5)


class SubscriptionsViewTest(ViewTestsTemplate):
    @override_settings(SUBSCRIPTION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_subscriptions_list(self):
        """
        Doing a GET request should return a page of subscriptions.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_subscriptions_callback(num=10)
        self.add_messagesets_callback([{'id': 1, 'short_name': 'ms.1'}])

        response = self.client.get(reverse('subscriptions'))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['subscriptions']), 5)

    @override_settings(SUBSCRIPTION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_subscriptions_list_filter_error(self):
        """
        If the data submitted for filtering the list of subscriptions is
        invalid, then the errors should be sent in the form, as well as an
        empty list of subscriptions.
        """
        self.login()
        self.set_session_user_tokens()
        self.add_messagesets_callback([{'id': 1, 'short_name': 'ms.1'}])

        qs = "?identity=&active=invalid&completed="
        response = self.client.get('{}{}'.format(reverse('subscriptions'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['subscriptions']), 0)
        self.assertFalse(context['form'].is_valid())
        self.assertEqual(len(context['form'].errors), 1)

    @override_settings(SUBSCRIPTION_LIST_PAGE_SIZE=5)
    @responses.activate
    def test_get_filtered_subscriptions_list(self):
        """
        If there are query parameters for filtering the list of subscriptions,
        then that list should be filtered.
        """
        self.login()
        self.set_session_user_tokens()
        qs = "?completed=True&identity=1234&active=True"
        self.add_subscriptions_callback(num=10, qs=qs)
        self.add_messagesets_callback([{'id': 1, 'short_name': 'ms.1'}])

        response = self.client.get('{}{}'.format(reverse('subscriptions'), qs))
        context = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context['subscriptions']), 5)


class UserDetailViewTest(ViewTestsTemplate):

    def setUp(self):
        self.login()
        self.set_session_user_tokens()

    @responses.activate
    def test_get_user_detail(self):
        """
        Doing a GET request should return a page of the user detail.
        """
        self.add_identity_callback(
            'identity_id', {
                'preferred_language': "zul_ZA",
                'linked_to': "linked_to_identity",
                'operator': "operator_id"
            })
        self.add_identity_callback('linked_to_identity', {})
        self.add_identity_callback('operator_id')
        self.add_messagesets_callback([{
            'id': 1,
            'short_name': 'ms.1',
            'default_schedule': 2,
        }])
        self.add_registrations_callback(qs="?mother_id=identity_id")
        self.add_subscriptions_callback(num=10, qs="?identity=identity_id")

        response = self.client.get(reverse('user-management-detail',
                                   kwargs={'identity': 'identity_id'}))
        context = response.context

        self.assertEqual(response.status_code, 200)

        self.assertEqual(context['identity']['details']['preferred_language'],
                         "zul_ZA")
        self.assertEqual(context['messagesets'], {1: "ms.1"})
        self.assertEqual(context['linked_to']['identity'],
                         "linked_to_identity")
        self.assertEqual(context['operator']['identity'],
                         "operator_id")
