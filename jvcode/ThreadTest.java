class B extends Thread{
   public void run(){
         for(int i=0;i<5;i++){
             System.out.println("From thread B"+ i);
         }
         System.out.println("Exit from B");
     }
     }
class A extends Thread{
   public void run(){
         for(int i=0;i<5;i++){
             System.out.println("From thread A"+ i);
         }
         System.out.println("Exit from A");
     }
     }
class ThreadTest {
    public static void main(String args[]) {
   A obja = new A();
   B objb = new B();
   obja.start(); 
   objb.start();
 

    }
}