# On-Device Training

## Why Train on Edge?
1.  **Privacy**: Keyboard apps (Gboard) learn new words without sending keystrokes to Google.
2.  **Personalization**: FaceID learns *your* face changes (glasses/beard) over time.
3.  **Bandwidth**: Don't upload raw data. Upload *gradients*.

## Federated Learning
1.  Server sends Global Model ($M_G$) to devices.
2.  Device $k$ trains locally on private data $D_k$ -> Update $\Delta W_k$.
3.  Device sends $\Delta W_k$ to Server.
4.  Server averages updates: $W_{new} = W_{old} + \alpha \sum \Delta W_k$.

## Transfer Learning on Edge
-   Freeze the "Backbone" (MobileNet layers 1-100).
-   Retrain only the "Head" (Final Dense Layer) on the device.
-   Cheap: Only forward prop + backprop on 1 layer.
