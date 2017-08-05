package main;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;

public class DashboardController {
    @FXML
    private Button startButton;
    @FXML
    private Slider t1Slider;
    @FXML
    private Slider t2Slider;
    @FXML
    private Slider h1Slider;
    @FXML
    private Slider h2Slider;
    @FXML
    private Slider m1Slider;
    @FXML
    private Slider m2Slider;
    @FXML
    private Slider wSlider;
    @FXML
    private Label l1;
    @FXML
    private Label l2;

    @FXML
    private void initialize(){
        l1.setText("Crop 1");
        l2.setText("Crop 2");

        startButton.setOnAction(event -> {
            int t1 = 10 - (int) t1Slider.getValue();
            int t2 = 10 - (int) t2Slider.getValue();
            int h1 = 10 - (int) h1Slider.getValue();
            int h2 = 10 - (int) h2Slider.getValue();
            int m1 = (int) m1Slider.getValue();
            int m2 = (int) m2Slider.getValue();
            int w = (int) wSlider.getValue();

            HTTP http = new HTTP();

            System.out.println("Testing 1 - Send Http GET request");
            try {
                double d1 = http.sendGet(1, t1, h1, m1);
                double d2 = http.sendGet(2, t2, h2, m2);

                d1 = (double)Math.round(d1 * 1000d) / 1000d;
                d2 = (double)Math.round(d2 * 1000d) / 1000d;

                System.out.println(d1);
                System.out.println(d2);

                String s1 = formatter(d1);
                String s2 = formatter(d2);

                l1.setText(s1);
                l2.setText(s2);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public static String formatter(double d){
        return String.valueOf(d / 2) + " minutes";
    }
}