#include <Python.h>
#include "Firebase.h"
#include "FirebaseAnalytics.h"
#include "FirebaseAdmob.h"
#include "FirebaseAuth.h"
#include "FirebaseMessaging.h"

typedef struct {
	PyObject_HEAD
		Firebase* firebase;
} firebase_obj;

typedef struct {
	PyObject_HEAD
		FirebaseAnalytics* firebaseAnalytics;
} firebaseAnalytics_obj;

typedef struct {
	PyObject_HEAD
		FirebaseAdmob* firebaseAdmob;
} firebaseAdmob_obj;

typedef struct {
	PyObject_HEAD
		FirebaseAuth* firebaseAuth;
} firebaseAuth_obj;

typedef struct {
	PyObject_HEAD
		FirebaseMessaging* firebaseMessaging;
} firebaseMessaging_obj;

extern PyTypeObject FirebaseType;
extern PyTypeObject FirebaseAnalyticsType;
extern PyTypeObject FirebaseAdmobType;
extern PyTypeObject FirebaseAuthType;
extern PyTypeObject FirebaseMessagingType;
