package main;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
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
    private void initialize(){
        startButton.setOnAction(event -> {
            int t1 = (int) t1Slider.getValue();
            int t2 = (int) t2Slider.getValue();
            int h1 = (int) h1Slider.getValue();
            int h2 = (int) h2Slider.getValue();
            int m1 = (int) m1Slider.getValue();
            int m2 = (int) m2Slider.getValue();
            int w = (int) wSlider.getValue();

            HTTP http = new HTTP();

            System.out.println("Testing 1 - Send Http GET request");
            try {
                http.sendGet(1, t1, h1, m1);
                http.sendGet(2, t2, h2, m2);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }
}