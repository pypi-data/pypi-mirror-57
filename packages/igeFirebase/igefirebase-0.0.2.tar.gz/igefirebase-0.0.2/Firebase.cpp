#include "Firebase.h"
#include "firebase/app.h"
#include "firebase/future.h"
#include "firebase/admob.h"

#ifdef _WIN32
#include <windows.h>
#include <stdarg.h>

WindowContext FirebaseGetWindowContext()
{
	return nullptr;
}

static LARGE_INTEGER	freq;

#elif defined(__ANDROID__)
#include <unistd.h>
#include <jni.h>
#include "SDL.h"

JNIEnv* FirebaseGetJniEnv()
{
	return (JNIEnv*)SDL_AndroidGetJNIEnv();
}

jobject FirebaseGetActivity()
{
    return (jobject)SDL_AndroidGetActivity();
}

// Get the window context. For Android, it's a jobject pointing to the Activity.
jobject FirebaseGetWindowContext()
{
	return FirebaseGetActivity();
}
#elif defined(__APPLE__)
#include <unistd.h>
#include <stdarg.h>

extern "C" WindowContext GetWindowContext();
WindowContext FirebaseGetWindowContext()
{
	return GetWindowContext();
}

#endif

::firebase::App* Firebase::firebase_app = nullptr;

Firebase::Firebase()
{
#if defined _WIN32
	QueryPerformanceFrequency(&freq);
#endif
}
Firebase::~Firebase()
{
}

void Firebase::init()
{
	firebase_app = ::firebase::App::GetInstance();

	if (firebase_app == nullptr)
	{
		LOG("Initialize the Firebase library");
        FirebasePlatformInit();
	}
	
	LOG("fb.initCreated the firebase app %x", static_cast<int>(reinterpret_cast<intptr_t>(firebase_app)));	
	
}

void Firebase::release()
{
	LOG("release");
	delete firebase_app;
}

void Firebase::WaitForFutureCompletion(firebase::FutureBase future, int msec, double timeout)
{
    double time = GetTime();
    while (!FirebaseProcessEvents(msec)) {
        double elapsedTime =  GetTime() - time;
        if (future.status() != firebase::kFutureStatusPending || elapsedTime > timeout) {
            break;
        }
    }

    if (future.error() != firebase::admob::kAdMobErrorNone) {
      LOG("ADMOB ERROR: Action failed with error code %d and message \"%s\".\n",
                 future.error(), future.error_message());
    }
}

double Firebase::GetTime()
{
#if defined _WIN32
    static LARGE_INTEGER	cuurentTime;	
	QueryPerformanceCounter(&cuurentTime);
	return (double)cuurentTime.QuadPart / (double)freq.QuadPart;
#elif defined __ANDROID__
    struct timespec tv;
    clock_gettime(CLOCK_MONOTONIC, &tv);
    return (double)tv.tv_sec + (double)tv.tv_nsec / 1000000000.0;
#else
    uint64_t t = mach_absolute_time();
        double tsec = (double)t * (double)base.numer / (double)base.denom / 1000000000.0;
		return tsec;
#endif
}
