package main;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
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
    private Slider w1Slider;
    @FXML
    private Slider w2Slider;

    @FXML
    private void initialize(){
        startButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                int t1 = (int) t1Slider.getValue();
                int t2 = (int) t2Slider.getValue();
                int h1 = (int) h1Slider.getValue();
                int h2 = (int) h2Slider.getValue();
                int m1 = (int) m1Slider.getValue();
                int m2 = (int) m2Slider.getValue();
                int w1 = (int) w1Slider.getValue();
                int w2 = (int) w2Slider.getValue();
            }
        });
    }
}