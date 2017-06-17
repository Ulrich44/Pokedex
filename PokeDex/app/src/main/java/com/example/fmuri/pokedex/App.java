package com.example.fmuri.pokedex;

import android.app.Application;
import android.media.MediaPlayer;

/**
 * Created by rmadrigal on 5/30/17.
 */

public final class App extends Application {
    private static App sInstance;
    private byte[] mCapturedPhotoData;
    private MediaPlayer mMediaPlayer;

    public byte[] getCapturedPhotoData() {
        return mCapturedPhotoData;
    }

    public void setCapturedPhotoData(byte[] capturedPhotoData) {
        mCapturedPhotoData = capturedPhotoData;
    }

    // Singleton code
    public static App getInstance() { return sInstance; }

    @Override
    public void onCreate() {
        super.onCreate();
        sInstance = this;

        mMediaPlayer = MediaPlayer.create(this, R.raw.music);
        mMediaPlayer.setLooping(true);
        mMediaPlayer.start();
    }

    @Override
    public void onTerminate() {
        super.onTerminate();

        mMediaPlayer.stop();
    }
}
