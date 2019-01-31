String serIn; 
int ABS = 150;
int in1 = 6; 
int in2 = 7; 
int in3 = 8; 
int in4 = 9; 
int ENA = 10; 
int ENB = 11; 
int PIRPin = 12; 

 void _mForwardA() //manera de mover hacia adelante el motor de las pastillas A 
 {
  analogWrite(ENA,ABS); 
  //analogWrite(ENB,ABS); 
  digitalWrite(in1,HIGH);//digital output 
  digitalWrite(in2,LOW); 
  } 
  
   void _mForwardB() //manera de mover hacia adelante el motor de las pastillas B 
   { 
    //analogWrite(ENA,ABS); 
    analogWrite(ENB,ABS); 
    digitalWrite(in3,HIGH);//digital output 
    digitalWrite(in4,LOW); 
    } 

void _mBackA() //manera de mover hacia atrás el motor de las pastillas A 
{ 
  analogWrite(ENA,ABS); 
  //analogWrite(ENB,ABS); 
  digitalWrite(in1,LOW); 
  digitalWrite(in2,HIGH); 
  } 
  
  void _mBackB() //manera de mover hacia atrás el motor de las pastillas B 
  { 
    //analogWrite(ENA,ABS); 
    analogWrite(ENB,ABS); 
    digitalWrite(in3,LOW); 
    digitalWrite(in4,HIGH); 
    } 
    
    void _mStop() //Método usado para detener los motores 
    { 
      digitalWrite(ENA,LOW); 
      digitalWrite(ENB,LOW); 
      } 
      
void setup() { 
  // put your setup code here, to run once: 
  Serial.begin(9600); 
  while (Serial.available()>0){ 
    serIn=Serial.read(); 
    } 
    pinMode(in1,OUTPUT); 
    pinMode(in2,OUTPUT); 
    pinMode(in3, OUTPUT); 
    pinMode(in4, OUTPUT); 
    pinMode(ENA,OUTPUT); 
    pinMode(ENB,OUTPUT); 
    pinMode(PIRPin, INPUT); 
    _mStop(); 
    } 
          
          
void loop() { 
  // put your main code here, to run repeatedly: 
  String nombre_pastilla; 
  String dosis; 
  int val = digitalRead(PIRPin); 
  if (Serial.available()>0){ 
    serIn = Serial.read(); 
if (serIn == "A"){ 
_mForwardA();  
  if (val == HIGH){
    _mStop(); }
  }
else if (serIn == "B"){
  _mForwardB();
  if(val == HIGH){
    _mStop();
    }
  }
  }  
} 
