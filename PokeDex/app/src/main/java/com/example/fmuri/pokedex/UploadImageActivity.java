package com.example.fmuri.pokedex;

import android.app.ProgressDialog;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.nfc.Tag;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

import com.goebl.david.Webb;

import java.io.ByteArrayOutputStream;

public class UploadImageActivity extends AppCompatActivity {
    private static final String TAG = UploadImageTask.class.getSimpleName();
    private EditText mPokemonNameInput;
    private ImageButton mUploadButton;
    private ImageView mPreviewImage;
    private ProgressDialog mProgressDialog;
    private UploadImageTask mUploadImageTask;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_upload_image);

        mPokemonNameInput = (EditText) findViewById(R.id.upload_image_pokemon_name_input);
        mPreviewImage = (ImageView) findViewById(R.id.upload_image_pokemon_preview);
        mUploadButton = (ImageButton) findViewById(R.id.upload_image_pokemon_upload_btn);

        byte[] imageData = App.getInstance().getCapturedPhotoData();
        final Bitmap bitmap = rotate(BitmapFactory.decodeByteArray(imageData, 0, imageData.length), 90);
        mPreviewImage.setImageBitmap(bitmap);

        mUploadButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String pokemonName = mPokemonNameInput.getText().toString();
                String progressMsg = "Subiendo imagen " + pokemonName + " a servidor";
                mProgressDialog = ProgressDialog.show(UploadImageActivity.this, "", progressMsg, true);
                try {
                    ByteArrayOutputStream baos = new ByteArrayOutputStream();
                    bitmap.compress(Bitmap.CompressFormat.JPEG, 60, baos);
                    String encodedImage = Base64.encodeToString(baos.toByteArray(), Base64.DEFAULT);

                    mUploadImageTask = new UploadImageTask(pokemonName, encodedImage);
                    mUploadImageTask.execute((Void) null);
                }catch (Exception ex){
                    Log.e(TAG, ex.getLocalizedMessage(), ex);
                }
            }
        });
    }

    public static Bitmap rotate(Bitmap bitmap, int degree) {
        int w = bitmap.getWidth();
        int h = bitmap.getHeight();

        Matrix mtx = new Matrix();
        mtx.postRotate(degree);

        return Bitmap.createBitmap(bitmap, 0, 0, w, h, mtx, true);
    }

    private class UploadImageTask extends AsyncTask<Void, Void, Boolean>{
        private String mPokemonName;
        private String mBase64Image;

        UploadImageTask(String pokemonName, String base64Image){
            this.mPokemonName = pokemonName;
            this.mBase64Image = base64Image;
        }


        @Override
        protected Boolean doInBackground(Void... params) {
            try {
                Webb webb = Webb.create();
                String response = webb.post("http://172.19.13.241:80/api/v1/pokemon")
                        .param("pokemon", mPokemonName)
                        .param("photo", mBase64Image)
                        .asString()
                        .getBody();
                return response.equals("true");
            } catch (Exception ex){
                Log.e(TAG, ex.getLocalizedMessage(), ex);
                return false;
            }
        }

        @Override
        protected void onPostExecute(Boolean success) {
            if (mProgressDialog != null){
                mProgressDialog.dismiss();
                mProgressDialog = null;
            }

            if (success){
                Toast.makeText(getApplicationContext(), "Pokemon almacenado en servidor", Toast.LENGTH_LONG).show();
                finish();
            } else {
                Toast.makeText(getApplicationContext(), "No se pudo subir la imagen", Toast.LENGTH_LONG).show();
            }
        }
    }
}
