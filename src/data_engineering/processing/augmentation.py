from typing import List
import random

class TextAugmenter:
    """
    Simple text augmentation techniques for NLP.
    """
    
    @staticmethod
    def synonym_replacement(text: str, synonyms: Dict[str, List[str]], n: int = 1) -> str:
        words = text.split()
        new_words = words.copy()
        random_word_list = list(set([word for word in words if word in synonyms]))
        random.shuffle(random_word_list)
        
        num_replaced = 0
        for random_word in random_word_list:
            syns = synonyms[random_word]
            if len(syns) >= 1:
                synonym = random.choice(syns)
                new_words = [synonym if word == random_word else word for word in new_words]
                num_replaced += 1
            if num_replaced >= n:
                break
                
        return " ".join(new_words)

class ImageAugmenter:
    """
    Mock image augmentation (usually done with albumentations/torchvision).
    """
    @staticmethod
    def random_crop(image_array: Any, size: tuple):
        print(f"Cropping image to {size}")
        return image_array # Placeholder
