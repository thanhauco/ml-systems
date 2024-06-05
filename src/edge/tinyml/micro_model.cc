/*
 * micro_model.cc
 * 
 * Example C++ code for invoking TFLite Micro on a microcontroller.
 */

#include "tensorflow/lite/micro/all_ops_resolver.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"

// The model data (converted via xxd)
extern const unsigned char g_model[];
extern const int g_model_len;

namespace {
  tflite::ErrorReporter* error_reporter = nullptr;
  const tflite::Model* model = nullptr;
  tflite::MicroInterpreter* interpreter = nullptr;
  TfLiteTensor* input = nullptr;
  TfLiteTensor* output = nullptr;

  // Tensor Arena (Memory pool)
  constexpr int kTensorArenaSize = 2 * 1024;
  uint8_t tensor_arena[kTensorArenaSize];
}

void setup() {
  model = tflite::GetModel(g_model);
  static tflite::AllOpsResolver resolver;
  static tflite::MicroInterpreter static_interpreter(
      model, resolver, tensor_arena, kTensorArenaSize, error_reporter);
  interpreter = &static_interpreter;

  interpreter->AllocateTensors();
  input = interpreter->input(0);
  output = interpreter->output(0);
}

void loop() {
  // 1. Fill Input Buffer
  input->data.f[0] = 0.5f;

  // 2. Invoke
  interpreter->Invoke();

  // 3. Read Output
  float prediction = output->data.f[0];
}
