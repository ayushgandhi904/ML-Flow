import mlflow

def calculate_sum(x, y):
    return x*y

if __name__ == "__main__":
    #Server starting of the ml flow
    with mlflow.start_run():
        x,y = 10, 20
        z = calculate_sum(x, y)
        #tracking experiment 
        mlflow.log_param("x", x)
        mlflow.log_param("y", y)
        mlflow.log_metric("z", z)