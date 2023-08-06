#include "Firebase.h"
#include "FirebaseAdmob.h"

#include "firebase/admob.h"
#include "firebase/admob/banner_view.h"
#include "firebase/admob/interstitial_ad.h"
#include "firebase/admob/rewarded_video.h"
#include "firebase/admob/types.h"
#include "firebase/app.h"
#include "firebase/future.h"

#include <windows.h>

// --- caching for fast access ---
static firebase::admob::BannerView* s_banner;
firebase::admob::InterstitialAd* s_interstitial;

void FirebaseLogMessage(const char* format, ...) {
	va_list list;
	va_start(list, format);
	vprintf(format, list);
	va_end(list);
	printf("\n");
	fflush(stdout);
}

bool FirebaseProcessEvents(int msec)
{
    Sleep(msec);
    return false;
}

void FirebasePlatformInit()
{
    Firebase::firebase_app = ::firebase::App::GetInstance();
    if(Firebase::firebase_app == nullptr)
    {
        Firebase::firebase_app = ::firebase::App::Create();    
    }
}

void PlatformAdmobInit(const char* admobAppID, const char* bannerAdUnit, const char* interstitialAdUnit, firebase::admob::AdSize banner_ad_size)
{
    LOG("Initializing the AdMob with Firebase API.");
    firebase::admob::Initialize(*Firebase::firebase_app, admobAppID);

    LOG("Initializing the AdMob banner.");
    s_banner = new firebase::admob::BannerView();
    s_banner->Initialize(FirebaseGetWindowContext(), bannerAdUnit, banner_ad_size);
    Firebase::WaitForFutureCompletion(s_banner->InitializeLastResult());

    LOG("Initializing rewarded video.");
    namespace rewarded_video = firebase::admob::rewarded_video;
    rewarded_video::Initialize();
    Firebase::WaitForFutureCompletion(rewarded_video::InitializeLastResult());

    LOG("Initializing interstitial video.");
    s_interstitial = new firebase::admob::InterstitialAd();
    s_interstitial->Initialize(FirebaseGetWindowContext(), interstitialAdUnit);
    Firebase::WaitForFutureCompletion(s_interstitial->InitializeLastResult());

}

void PlatformAdmobListener(FirebaseAdmob::LoggingBannerViewListener* banner_listener, FirebaseAdmob::LoggingRewardedVideoListener* rewarded_listener, FirebaseAdmob::LoggingInterstitialAdListener* interstitial_listener)
{
    s_banner->SetListener(banner_listener);
    s_interstitial->SetListener(interstitial_listener);
    firebase::admob::rewarded_video::SetListener(rewarded_listener);
}

void PlatformAdmobRelease()
{
    delete s_banner;
    delete s_interstitial;
    firebase::admob::rewarded_video::Destroy();
    firebase::admob::Terminate();
}

void PlatformShowBaner(firebase::admob::AdRequest request, firebase::admob::BannerView::Position position)
{
    // Load the banner ad.
    LOG("Loading a banner ad.");
    s_banner->LoadAd(request);
    Firebase::WaitForFutureCompletion(s_banner->LoadAdLastResult());

    // Make the BannerView visible.
    LOG("Showing the banner ad.");
    s_banner->Show();
    s_banner->MoveTo(position);
}

void PlatformShowBaner(firebase::admob::AdRequest request, int x, int y)
{
    // Load the banner ad.
    LOG("Loading a banner ad.");
    s_banner->LoadAd(request);
    Firebase::WaitForFutureCompletion(s_banner->LoadAdLastResult());

    // Make the BannerView visible.
    LOG("Showing the banner ad.");
    s_banner->Show();
    s_banner->MoveTo(x, y);
}

void PlatformHideBaner()
{
    s_banner->Hide();
}

void PlatformBanerMoveTo(firebase::admob::BannerView::Position position)
{
    s_banner->MoveTo(position);
    Firebase::WaitForFutureCompletion(s_banner->MoveToLastResult());
}

void PlatformBanerMoveTo(int x, int y)
{
    s_banner->MoveTo(x, y);
    Firebase::WaitForFutureCompletion(s_banner->MoveToLastResult());
}

void PlatformShowInterstitial(const char* interstitialAdUnit, firebase::admob::AdRequest request)
{
    s_interstitial->LoadAd(request);
    Firebase::WaitForFutureCompletion(s_interstitial->LoadAdLastResult());

    // When the InterstitialAd has loaded an ad, show it.
    LOG("Showing the interstitial ad.");
    s_interstitial->Show();
    Firebase::WaitForFutureCompletion(s_interstitial->ShowLastResult());
}

void PlatformShowRewardedVideo(const char* rewardedVideoAdUnit, firebase::admob::AdRequest request)
{
    namespace rewarded_video = firebase::admob::rewarded_video;
    
    LOG("Loading a rewarded video ad.");
    rewarded_video::LoadAd(rewardedVideoAdUnit, request);
    Firebase::WaitForFutureCompletion(rewarded_video::LoadAdLastResult());
    
    if (rewarded_video::LoadAdLastResult().error() == firebase::admob::kAdMobErrorNone)
    {
      LOG("Showing a rewarded video ad.");
      rewarded_video::Show(FirebaseGetWindowContext());
      Firebase::WaitForFutureCompletion(rewarded_video::ShowLastResult());
    }
}
