
using System;
class HelloWorld {
  static void Main() {
      //الترحيب
      
    Console.WriteLine("welcome to my application");
    Console.WriteLine("to have a resolt you shold enter the values");
    
    
    //المدخلات والتحويلات
    Console.WriteLine("enter the first number: ");
    int first_number =int.Parse(Console.ReadLine());    
    Console.WriteLine("chois a pross -  +  *  /  ")  ;
    string pross= Console.ReadLine();
    Console.WriteLine("enter the second number:");
    int second_number=int.Parse(Console.ReadLine());
    
    //التنفيذ لاستخراج الناتج
    
    switch (pross){
        case("+"): 
        Console.WriteLine(first_number +second_number);
        break;
        case ("-"):
            Console.WriteLine(first_number-second_number);
            break;
        case("*") :
            Console.WriteLine(first_number*second_number);
            break;
        case ("/"):
            Console.WriteLine(first_number/second_number);
            break;
    }
      
      
      
      
      
      
      
      
  }
}
