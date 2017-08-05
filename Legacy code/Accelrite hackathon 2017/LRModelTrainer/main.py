import data_generator
import learn

if __name__ == '__main__':
    # Generate sample data
    data_generator.generate_data()

    # Train the linear regression model
    learn.train_model()
