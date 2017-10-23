const int NUM_BYTES = 4;
byte data[NUM_BYTES];
void setup() {
        // Se establece la conexión serial
	Serial.begin(9600);
}
 
void loop(){
    serialPy();
	/*if (Serial.available() > 0) {
		if (Serial.read() == 107) { 
                        Serial.println(107);
                        pinMode(13,HIGH);
                        delay(10);
                        // Se envia el caracter 445.45
			Serial.println(445.45);
		}
	}
        pinMode(13, LOW);
                delay(10);
                */
}
void serialPy ()
{
   if (Serial.available() > 0) {
		if (Serial.read() == 107) { 
                        delay(4);
                        // Se envia el caracter 445.45
			Serial.println(445.45);
		}
	}
}
