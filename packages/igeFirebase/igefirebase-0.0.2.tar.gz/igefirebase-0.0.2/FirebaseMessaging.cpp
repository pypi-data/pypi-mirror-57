#include "FirebaseMessaging.h"

#include "firebase/app.h"
#include "firebase/future.h"
#include "firebase/messaging.h"
#include "firebase/util.h"

FirebaseMessaging::FirebaseMessaging()
	: m_listener(nullptr)
	, m_initializer(nullptr)
{
	LOG("FirebaseMessaging()");
}
FirebaseMessaging::~FirebaseMessaging()
{
	LOG("~FirebaseMessaging()");
}

void FirebaseMessaging::init()
{
	LOG("Initialize the Messaging library");

	m_initializer = new ::firebase::ModuleInitializer();
	m_listener = new ::firebase::messaging::PollableListener();
	
	m_initializer->Initialize(
		firebase_app, m_listener, [](::firebase::App* app, void* userdata) {
			LOG("Try to initialize Firebase Messaging");
			::firebase::messaging::PollableListener* listener =
				static_cast<::firebase::messaging::PollableListener*>(userdata);
			firebase::messaging::MessagingOptions options;
			// Prevent the app from requesting permission to show notifications
			// immediately upon starting up. Since it the prompt is being
			// suppressed, we must manually display it with a call to
			// RequestPermission() elsewhere.
			options.suppress_notification_permission_prompt = true;

			return ::firebase::messaging::Initialize(*app, listener, options);
		});

	while (m_initializer->InitializeLastResult().status() !=
		firebase::kFutureStatusComplete) {
		if (FirebaseProcessEvents(100)) return;  // exit if requested
	}
	if (m_initializer->InitializeLastResult().error() != 0) {
		LOG("Failed to initialize Firebase Messaging: %s",
			m_initializer->InitializeLastResult().error_message());
		FirebaseProcessEvents(2000);
		return;
	}

	// This will display the prompt to request permission to receive notifications
	// if the prompt has not already been displayed before. (If the user already
	// responded to the prompt, their decision is cached by the OS and can be
	// changed in the OS settings).
	::firebase::Future<void> result = ::firebase::messaging::RequestPermission();
	LOG("Display permission prompt if necessary.");
	while (result.status() == ::firebase::kFutureStatusPending) {
		FirebaseProcessEvents(100);
	}
	if (result.error() ==
		::firebase::messaging::kErrorFailedToRegisterForRemoteNotifications) {
		LOG("Error registering for remote notifications.");
	}
	else {
		LOG("Finished checking for permission.");
	}

	LOG("Initialized Firebase Cloud Messaging.");

	std::string token;
	if (m_listener && m_listener->PollRegistrationToken(&token)) {
		LOG("Received Registration Token: %s", token.c_str());
	}
}

void FirebaseMessaging::release()
{
	delete m_listener;
	delete m_initializer;
	::firebase::messaging::Terminate();
}

const char* FirebaseMessaging::getRegistrationToken()
{
	std::string token;
	if (m_listener && m_listener->PollRegistrationToken(&token)) {
		LOG("Received Registration Token: %s", token.c_str());
	}

	return token.c_str();
}
