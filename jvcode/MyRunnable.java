class A implements Runnable{
    public void run() {
        for(int i=0;i<5;i++){
            System.out.println("Main Thread");
        }
    }
}
public class MyRunnable {
    public static void main(String args[]) {
     A t = new A();

     // Thred obj1= new Thread();
     // obj1.start(); not give any output
     Thread obj = new Thread(t);
     obj.start();
     for(int i=0;i<5;i++){
         System.out.println("Anothr Thresas");
     }
    }
}
