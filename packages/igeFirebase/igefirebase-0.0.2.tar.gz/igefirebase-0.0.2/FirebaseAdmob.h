#pragma once
#include "Firebase.h"
#include "firebase/admob.h"
#include "firebase/admob/banner_view.h"

namespace admob = firebase::admob;
namespace rewarded_video = admob::rewarded_video;

typedef void (*AdmobHandlerFunc)(const char* adsType, int number, const char* reward);

class IGE_EXPORT FirebaseAdmob : public Firebase
{
public:
    static class LoggingRewardedVideoListener
            : public admob::rewarded_video::Listener {
    public:
        LoggingRewardedVideoListener() {}
        void OnRewarded(admob::rewarded_video::RewardItem reward) override {
            LOG("Rewarding user with %f %s.", reward.amount,
                reward.reward_type.c_str());
            m_HandlerFunc("RewardedVideo", reward.amount, reward.reward_type.c_str());
        }
        void OnPresentationStateChanged(
                admob::rewarded_video::PresentationState state) override {
            LOG("Rewarded video PresentationState has changed to %d.", state);
            m_HandlerFunc("RewardedVideo", state, "PresentationStateChanged");
        }
    };

    static class LoggingInterstitialAdListener
            : public admob::InterstitialAd::Listener {
    public:
        LoggingInterstitialAdListener() {}
        void OnPresentationStateChanged(
                admob::InterstitialAd* interstitial_ad,
                admob::InterstitialAd::PresentationState state) override {
            LOG("InterstitialAd PresentationState has changed to %d.", state);
            m_HandlerFunc("Interstitial", state, "PresentationStateChanged");
        }
    };

    static class LoggingBannerViewListener : public admob::BannerView::Listener {
    public:
        LoggingBannerViewListener() {}
        void OnPresentationStateChanged(
                admob::BannerView* banner_view,
                admob::BannerView::PresentationState state) override {
            LOG("BannerView PresentationState has changed to %d.", state);
            m_HandlerFunc("BannerView", state, "PresentationStateChanged");
        }
        void OnBoundingBoxChanged(admob::BannerView* banner_view,
                                  admob::BoundingBox box) override {
            LOG("BannerView BoundingBox has changed to (x: %d, y: %d, width: %d, height %d).", box.x, box.y, box.width, box.height);
        }
    };

public:
	FirebaseAdmob();
	~FirebaseAdmob();
	void init();
	void release();
	void testcase();

	//void showBanner(bool reload = true, int timeout = 1000);
    void showBanner(admob::BannerView::Position position);
    void showBanner(int x, int y);
	void bannerMoveTo(admob::BannerView::Position position);
	void bannerMoveTo(int x, int y);
	void hideBanner();

	void showInterstitial();

	void showRewardedVideo();
	void pauseRewardedVideo();
	void resumeRewardedVideo();

	void registerEventListener(AdmobHandlerFunc handler);

	void setAdMobApp(const char* adMobAppID, const char* bannerAdUnit, const char* interstitialAdUnit, const char* rewardedVideoAdUnit);
	void setBannerSize(uint32_t width, uint32_t height);
	void setGender(admob::Gender gender);
	void setChildDirectedTreatmentState(admob::ChildDirectedTreatmentState state);
	void setKeywords(uint32_t count, const char** keywords);
	void setTestDeviceIds(uint32_t count, const char** testDeviceIds);
	void setBirthday(uint32_t day, uint32_t month, uint32_t year);
private:
	const char* m_adMobAppID;
	const char* m_bannerAdUnit;
	const char* m_interstitialAdUnit;
	const char* m_rewardedVideoAdUnit;
	admob::Gender m_gender;
	admob::ChildDirectedTreatmentState m_childDirectedTreatmentState;
	uint32_t m_bannerWidth;
	uint32_t m_bannerHeight;
	const char** m_keywords;
	uint32_t m_keywordCount;
	const char** m_testDeviceIds;
	uint32_t m_testDeviceIdCount;
	uint32_t m_birthdayDay;
	uint32_t m_birthdayMonth;
	uint32_t m_birthdayYear;
    
    firebase::admob::AdRequest m_request;
    admob::AdSize m_banner_ad_size;

	LoggingBannerViewListener* m_banner_listener;
	LoggingInterstitialAdListener* m_interstitial_listener;
	LoggingRewardedVideoListener* m_rewarded_listener;

    static AdmobHandlerFunc m_HandlerFunc;
};

void PlatformAdmobInit(const char* admobAppID, const char* bannerAdUnit, const char* interstitialAdUnit, firebase::admob::AdSize banner_ad_size);
void PlatformAdmobRelease();
void PlatformShowBaner(firebase::admob::AdRequest request, firebase::admob::BannerView::Position position);
void PlatformShowBaner(firebase::admob::AdRequest request, int x, int y);
void PlatformHideBaner();
void PlatformBanerMoveTo(firebase::admob::BannerView::Position position);
void PlatformBanerMoveTo(int x, int y);
void PlatformShowInterstitial(const char* interstitialAdUnit, firebase::admob::AdRequest request);
void PlatformShowRewardedVideo(const char* rewardedVideoAdUnit, firebase::admob::AdRequest request);
void PlatformAdmobListener(FirebaseAdmob::LoggingBannerViewListener* banner_listener, FirebaseAdmob::LoggingRewardedVideoListener* rewarded_listener, FirebaseAdmob::LoggingInterstitialAdListener* interstitial_listener);
