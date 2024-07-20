# Security on the Edge

## Physical Access = Total Compromise?
If I can steal the robot, I can dump the flash memory.

## Risks
1.  **Model Theft**: Extracting your proprietary IP (the model weights) from the device.
2.  **Adversarial Attacks**: Putting a sticker on a Stop sign to make the car see "Speed Limit 60".
3.  **Sensor Spoofing**: Shining a laser into Lidar.

## Defenses
1.  **Secure Enclaves**: TrustZone (ARM). Run the model in TEE (Trusted Execution Environment).
2.  **Model Encryption**: Decrypt model only in RAM, or use hardware that decrypts on-the-fly.
3.  **Signed Updates**: Ensure firmware updates are signed by your private key.
