#include <WiFiS3.h>
#include "secrets.h"
WiFiUDP udp;

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>
Adafruit_BMP280 bmp; 
int redStrength=0;
int greenStrength=0;
int blueStrength=0;
int port=12345;
bool onr=0,onb=0,ong=0;
char myPacket[255];
int R=3,G=5,B=10;
String response="0";
String myString;
String stringArray[10];

void setup() {
  stringArray[1]="0";
  pinMode(R,OUTPUT);
  pinMode(G,OUTPUT);
  pinMode(B,OUTPUT);

  Serial.begin(9600);
  Serial.print("connecting to ");
  Serial.println(mySSID);
  WiFi.begin(mySSID,myPASS);
  while(WiFi.status()!=WL_CONNECTED){
    delay(100);
    Serial.print(".");

  }
Serial.println("\nConnected to Wifi");
while(WiFi.localIP() == IPAddress(0,0,0,0)){
  Serial.println(WiFi.localIP());
}
Serial.println(WiFi.localIP());
udp.begin(port);
Serial.print("udp set to port ");
Serial.println(port);
}
void loop() {
if(udp.parsePacket()){
  myString=udp.readStringUntil('\n');
  Serial.println("Recieved: "+myString);
  splitString();
  
  if(myString[0]=='b'){
  for(int i=0;i<5;i++){
  switch (myString[1]){
   case 'r':
    analogWrite(R,redStrength);
    delay(200);
    analogWrite(R,LOW);
    delay(200);
    response=String(redStrength);
    break;
   case 'g':
    analogWrite(G,greenStrength);
    delay(200);
    analogWrite(G,LOW);
    delay(200);
    response=String(greenStrength);
    break;
   case 'b':
    analogWrite(B,blueStrength);
    delay(200);
    analogWrite(B,LOW);
    delay(200);
    response=String(blueStrength);
    break;
    default: break;}
  }
  }
  else{
    if(myString[2]=='f'){
    switch(myString[myString.length()-2]){
    case 'R':
    analogWrite(R,LOW); onr=0; response=String(redStrength);
    break;
    case 'G':
    analogWrite(G,LOW); ong=0; response=String(greenStrength);
    break;
    case 'B':
    analogWrite(B,LOW); onb=0; response=String(blueStrength);
    break; }
    }
    
    else{
      Serial.println(myString[myString.length()-2]);
      
    switch(myString[myString.length()-2]){
    case 'R':
    analogWrite(R,redStrength); onr=1; response=String(redStrength);
    break;
    case 'G':
    analogWrite(G,greenStrength); ong =1; response=String(greenStrength);
    break;
    case 'B':
    analogWrite(B,blueStrength); onb =1; response=String(blueStrength);
    break; 
    default: break;
    }}
  }
  udp.beginPacket(udp.remoteIP(),udp.remotePort());
  udp.print(response);
  udp.endPacket();
  Serial.println("Sent:" +response);


}
if(stringArray[0]=="redStrength") {response=stringArray[1]; redStrength=stringArray[1].toInt();}
if(stringArray[0]=="blueStrength") {response=stringArray[1]; blueStrength=stringArray[1].toInt();}
if(stringArray[0]=="greenStrength") {response=stringArray[1]; greenStrength=stringArray[1].toInt();}
if(onr)analogWrite(R,redStrength); 
if(onb)analogWrite(B,blueStrength); 
if(ong)analogWrite(G,greenStrength);

}

void splitString() {
myString=myString+":";
int i=0;
int start=0;
int indexCount=0;
for(int i=0;i<myString.length();i++){
  if(myString[i]==':'){
    stringArray[indexCount]=myString.substring(start,i);
    indexCount++; start=i+1;
  }
}
for(int i=0;i<indexCount;i++){
  Serial.println(stringArray[i]);
}
}
