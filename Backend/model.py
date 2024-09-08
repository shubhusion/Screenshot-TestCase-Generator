import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 8

def generate_test_cases(context, image_paths):
    try:
        images = []
        for image_path in image_paths:
            with Image.open(image_path) as img:
                img = img.convert('RGB')  # Ensure image is in RGB format
                images.append(img)
        
        logging.info(f"Processed {len(images)} images")
        
        pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)
        
        # Generate attention mask (assuming no padding needed for your case)
        attention_mask = torch.ones(pixel_values.shape[:2], device=device)
        
        output_ids = model.generate(
            pixel_values,
            attention_mask=attention_mask,  # Pass the attention mask
            max_length=max_length,
            num_beams=num_beams,
            return_dict_in_generate=True,
        )

        preds = tokenizer.batch_decode(output_ids.sequences, skip_special_tokens=True)
        preds = [pred.strip() for pred in preds]
        
        logging.info(f"Generated {len(preds)} predictions")

        # Generate test cases
        test_cases = [
            {
                "description": f"Test case for {pred}",
                "pre_conditions": "Ensure the app is installed and running",
                "testing_steps": ["Step 1: Open the app", f"Step 2: Navigate to the {pred} screen"],
                "expected_result": f"The {pred} functionality should work as expected"
            }
            for pred in preds
        ]

        return test_cases
    except Exception as e:
        logging.error(f"Error in generate_test_cases: {str(e)}")
        raise