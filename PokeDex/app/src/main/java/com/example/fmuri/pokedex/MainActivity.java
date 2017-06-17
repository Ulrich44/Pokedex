package com.example.fmuri.pokedex;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.hardware.Camera;
import android.nfc.Tag;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.ContextMenu;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity
        implements SurfaceHolder.Callback {

    private static final String TAG = MainActivity.class.getSimpleName();
    private Camera mCamera;
    private SurfaceView mSurfaceView;
    private SurfaceHolder mSurfaceHolder;

    private ImageView mBackground;
    private boolean isPokedexOn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mBackground = (ImageView) findViewById(R.id.background);
        mSurfaceView = (SurfaceView) findViewById(R.id.surfaceView);
        mSurfaceHolder = mSurfaceView.getHolder();
        mSurfaceHolder.addCallback(MainActivity.this);
        mSurfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);

        Button btnPower = (Button) findViewById(R.id.btn_power);
        btnPower.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startCamera();
            }
        });

        Button btnPicture = (Button) findViewById(R.id.btn_take_picture);
        btnPicture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isPokedexOn && mCamera != null) {
                    mCamera.takePicture(null, null, new Camera.PictureCallback() {
                        @Override
                        public void onPictureTaken(byte[] data, Camera camera) {
                            Toast.makeText(MainActivity.this, "Pokemon capturado", Toast.LENGTH_SHORT).show();
                            App.getInstance().setCapturedPhotoData(data);
                            startActivity(new Intent(MainActivity.this, UploadImageActivity.class));
                        }
                    });
                }

            }
        });
    }

    private void startCamera() {
        if (ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.CAMERA) !=
                PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.CAMERA}, 50);
        } else {
            try {
                if (mCamera != null) {
                    mCamera.release();
                    mCamera = null;

                }
                mCamera = Camera.open(Camera.CameraInfo.CAMERA_FACING_BACK);
            } catch (Exception ex) {
                Log.e(TAG, ex.getLocalizedMessage(), ex);
            }

            try {
                mCamera.setPreviewDisplay(mSurfaceHolder);
                mCamera.setDisplayOrientation(90);

                mCamera.startPreview();
                isPokedexOn = true;
                mBackground.setImageResource(R.drawable.bg_pokedex_on);
            } catch (Exception ex) {
                Log.e(TAG, ex.getLocalizedMessage(), ex);
            }


        }
    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {

    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {

    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {

    }
}
