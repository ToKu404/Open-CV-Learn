package com.example.open_cv_android;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import org.opencv.android.OpenCVLoader;
import org.opencv.android.Utils;
import org.opencv.core.Mat;
import org.opencv.core.Rect;
import org.opencv.imgproc.Imgproc;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.FileNotFoundException;
import java.io.InputStream;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private ImageView imageViewAmbil;
    private Button btnPilih, btnGrayscale, btnCropping, btnResizing, btnBlurring;
    private Bitmap bitmapAsli, bitmapGray, bitmapResized, bitmapCropped, bitmapBlurred;

    private static final String TAG = "CekOpenCV";
    private static final int IMAGE_PICK_CODE = 1000;
    private static final int PERMISSION_CODE = 1001;

    static {
        if (OpenCVLoader.initDebug()){
            Log.d(TAG, "Berhasil");

        }else{
            Log.d(TAG, "GAGAL");
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //VIEWS
        imageViewAmbil = findViewById(R.id.imageView);
        btnPilih = findViewById(R.id.btnPilihGambar);
        btnGrayscale = findViewById(R.id.btnGray);
        btnResizing = findViewById(R.id.btnResize);
        btnCropping = findViewById(R.id.btnCrop);
        btnBlurring = findViewById(R.id.btnBlur);


        btnPilih.setOnClickListener(this);
        btnGrayscale.setOnClickListener(this);
        btnResizing.setOnClickListener(this);
        btnBlurring.setOnClickListener(this);
        btnCropping.setOnClickListener(this);
    }


    private void ambilGambarGaleri(){
        Intent intent = new Intent(Intent.ACTION_PICK);
        intent.setType("image/*");
        startActivityForResult(intent, IMAGE_PICK_CODE);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        switch (requestCode) {
            case PERMISSION_CODE: {
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    ambilGambarGaleri();
                } else {
                    Toast.makeText(this, "Akses Ditolak", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == RESULT_OK && requestCode == IMAGE_PICK_CODE) {
            try {
                final Uri imageUri = data.getData();
                final InputStream imageStream = getContentResolver().openInputStream(imageUri);
                bitmapAsli = BitmapFactory.decodeStream(imageStream);
                imageViewAmbil.setImageBitmap(bitmapAsli);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
                Toast.makeText(this, "Ada yang salah", Toast.LENGTH_LONG).show();
            }
        }


    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.btnPilihGambar:
                handlePilihGambar();
                break;
            case R.id.btnGray:
                handlerGrayscale();
                break;
            case R.id.btnResize:
                handlerResizing();
                break;
            case R.id.btnBlur:
                handlerBluring();
                break;
            case R.id.btnCrop:
                handlerCroping();
                break;
        }
    }

    private void handlerCroping() {
        //Konvert bitmap ke bentuk matriks agar bisa diolah dengan OpenCV
        Mat matImageAwal = new Mat();
        Utils.bitmapToMat(bitmapAsli, matImageAwal);

        //Crop matriks dari gambar untuk ditampilkan di ImageView
        Rect areaCrop = new Rect(0, 0, 100,200);
        Mat matCropped = matImageAwal.submat(areaCrop);

        bitmapCropped = Bitmap.createBitmap(matCropped.cols(), matCropped.rows(), Bitmap.Config.ARGB_8888);
        Utils.matToBitmap(matCropped,bitmapCropped);

        //Menampilkan bitmap grayscale ke dalam ImageView
        imageViewAmbil.setImageBitmap(bitmapCropped);
    }

    private void handlerResizing() {
        //Resize bitmap menjadi ukuran 768x1024
        bitmapResized = Bitmap.createScaledBitmap(bitmapAsli, 400,300, true);

        //Menampilkan bitmap grayscale ke dalam ImageView
        imageViewAmbil.setImageBitmap(bitmapResized);
    }

    private void handlerBluring() {
        //PEmbuatan matriks baru yang kosong untuk menampung hasil konvert dari bitmap
        Mat matImageAwal = new Mat();
        Mat matBlurred = new Mat();

        //Merubah dari bitmap ke matriks untuk diolah menggunakan OpenCV
        Utils.bitmapToMat(bitmapAsli, matImageAwal);

        int kernelDimension = 25;
        Imgproc.medianBlur(matImageAwal, matBlurred, kernelDimension);

        bitmapBlurred = Bitmap.createBitmap(matBlurred.cols(), matBlurred.rows(), Bitmap.Config.ARGB_8888);
        Utils.matToBitmap(matBlurred, bitmapBlurred);

        //Menampilkan bitmap grayscale ke dalam ImageView
        imageViewAmbil.setImageBitmap(bitmapBlurred);
    }

    private void handlerGrayscale() {
        //PEmbuatan matriks baru yang kosong untuk menampung hasil konvert dari bitmap
        Mat matImageAwal = new Mat();
        Mat matGrayscaled = new Mat();

        //Merubah dari bitmap ke matriks untuk diolah menggunakan OpenCV
        Utils.bitmapToMat(bitmapAsli, matImageAwal);

        //Proses convert matriks bitmap asli menjadi grayscale
        Imgproc.cvtColor(matImageAwal, matGrayscaled, Imgproc.COLOR_BGR2GRAY);

        //Merubah matriks grayscale kedalam bentuk Bitmap
        bitmapGray = Bitmap.createBitmap(matGrayscaled.cols(), matGrayscaled.rows(), Bitmap.Config.ARGB_8888);
        Utils.matToBitmap(matGrayscaled, bitmapGray);

        //Menampilkan bitmap grayscale ke dalam ImageView
        imageViewAmbil.setImageBitmap(bitmapGray);
    }

    private void handlePilihGambar() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
            if (checkSelfPermission(Manifest.permission.READ_EXTERNAL_STORAGE)
                    == PackageManager.PERMISSION_DENIED){
                String[] permissions = {Manifest.permission.READ_EXTERNAL_STORAGE};
                requestPermissions(permissions, PERMISSION_CODE);
            }
            else {
                ambilGambarGaleri();
            }
        } else {
            ambilGambarGaleri();
        }
    }
}