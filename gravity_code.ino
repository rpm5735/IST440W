#include "HX711.h"
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;
HX711 scale;


void setup()
{
  lcd.begin(16, 2);
  Serial.begin(9600);
  delay(100);

  Serial.println("Weight ");
  Serial.println("Measuring...");
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(2280.f);
  scale.tare();
 
  lcd.print("Insert Weight");
  delay(100);
  lcd.clear();
 }

void loop()
{
  Serial.print("one reading:\t");
  Serial.print(scale.get_units(), 1);
  Serial.print("\t| average:\t");
  Serial.println(scale.get_units(10), 1);
  scale.power_down();     
  delay(100);
  scale.power_up();

  lcd.print("Weight :");
  delay(100);
  lcd.clear();
  delay(1);
 
  lcd.print(scale.get_units());   
  lcd.print("g");
  delay(100);
  lcd.clear();
  delay(1);
}
