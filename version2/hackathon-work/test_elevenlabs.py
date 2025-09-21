# # import os
# # from elevenlabs import ElevenLabs
# # from dotenv import load_dotenv

# # # Load your environment variables from .env file
# # load_dotenv()

# # # Get your API key from environment variables
# # api_key = os.getenv('ELEVENLABS_API_KEY')
# # print(f"API Key loaded: {api_key[:10]}...")  # Print first 10 chars for safety

# # # Initialize the client
# # try:
# #     client = ElevenLabs(api_key=api_key)
# #     print("✅ ElevenLabs client initialized successfully")
# # except Exception as e:
# #     print(f"❌ Failed to initialize client: {e}")
# #     exit()

# # # Test getting available voices (this verifies authentication)
# # try:
# #     voices = client.voices.get_all()
# #     print(f"✅ Authentication successful. Found {len(voices.voices)} voices")
# #     for voice in voices.voices[:3]:  # Print first 3 voices
# #         print(f"  - {voice.name} ({voice.voice_id})")
# # except Exception as e:
# #     print(f"❌ Authentication failed: {e}")
# #     exit()

# # # Test text-to-speech generation
# # test_text = "Hello, this is a test to see if the Eleven Labs API is working properly."
# # try:
# #     print(f"🧪 Generating audio for text: '{test_text}'")
    
# #     audio = client.text_to_speech(
# #         text=test_text,
# #         voice="Rachel",  # Use a voice you know exists
# #         model="eleven_monolingual_v1"
# #     )
    
# #     # Save the audio to a file
# #     with open("test_output.mp3", "wb") as f:
# #         f.write(audio)
    
# #     print("✅ Audio generated and saved successfully as 'test_output.mp3'")
# #     print("🎧 Play the file to verify the audio quality")

# # except Exception as e:
# #     print(f"❌ Text-to-speech generation failed: {e}")

# # import os
# # from elevenlabs import ElevenLabs
# # from dotenv import load_dotenv

# # load_dotenv()
# # api_key = os.getenv('ELEVENLABS_API_KEY')

# # print("🔍 Debugging the ElevenLabs client object...")

# # # Create the client
# # client = ElevenLabs(api_key=api_key)

# # # 1. Print the TYPE of the client
# # print(f"1. Type of client: {type(client)}")
# # print(f"   Module: {type(client).__module__}")

# # # 2. Print all attributes and methods the client has
# # print(f"\n2. All attributes/methods of client:")
# # for attr_name in dir(client):
# #     # Skip private attributes (ones starting with __)
# #     if not attr_name.startswith('__'):
# #         attr_value = getattr(client, attr_name)
# #         print(f"   - {attr_name} (type: {type(attr_value)})")

# # # 3. Check if text_to_speech exists
# # print(f"\n3. Has 'text_to_speech'? {hasattr(client, 'text_to_speech')}")
# # print(f"   Has 'generate'? {hasattr(client, 'generate')}")

# # # 4. Check if it's callable
# # print(f"\n4. Is client itself callable? {callable(client)}")

# import os
# from elevenlabs import ElevenLabs
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv('ELEVENLABS_API_KEY')

# client = ElevenLabs(api_key=api_key)

# test_text = "Hello, this is a test to see if the Eleven Labs API is working properly."

# try:
#     print(f"🧪 Generating audio using text_to_speech client...")
    
#     # Get the audio generator
#     audio_generator = client.text_to_speech.convert(
#         text=test_text,
#         voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel's voice ID
#         model_id="eleven_monolingual_v1"
#     )
    
#     # Collect all audio chunks from the generator
#     audio_chunks = []
#     for chunk in audio_generator:
#         audio_chunks.append(chunk)
    
#     # Combine all chunks into a single bytes object
#     audio_bytes = b''.join(audio_chunks)
    
#     # Save the complete audio file
#     with open("test_output.mp3", "wb") as f:
#         f.write(audio_bytes)
    
#     print("✅ Audio generated successfully! Saved as 'test_output.mp3'")

# except Exception as e:
#     print(f"❌ Failed: {e}")
#     import traceback
#     traceback.print_exc()


import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_nft_minting():
    print("🧪 Testing NFT Minting on Staging...")
    
    # Get credentials from .env
    api_key = os.getenv('CROSSMINT_API_KEY')
    collection_id = os.getenv('CROSSMINT_COLLECTION_ID')
    
    print(f"API Key: {api_key[:10]}...")
    print(f"Collection ID: {collection_id}")
    
    # Simple test metadata
    nft_metadata = {
        "name": "Test Proof of Debt",
        "description": "A test NFT to verify minting works on staging",
        "image": "https://ipfs.io/ipfs/QmX6z6Q7R8RZ5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z",  # You can use any test image URL
        "attributes": [
            {"trait_type": "Test", "value": "Successful"},
            {"trait_type": "Environment", "value": "Staging"}
        ]
    }
    
    headers = {
        "X-CLIENT-SECRET": api_key,
        "Content-Type": "application/json"
    }
    
    # Use a test wallet address (make sure it's a valid Solana devnet address)
    payload = {
        "recipient": "solana:6o4S6x4L3YVcmaeUaTt6pW7C5zL2X1vR8yK3dQ9bN2fM",  # Example devnet address
        "metadata": nft_metadata,
        "reuploadLinkedFiles": True
    }
    
    try:
        # Make sure to use STAGING URL
        response = requests.post(
            f"https://staging.crossmint.com/api/2022-06-09/collections/{collection_id}/nfts",
            headers=headers,
            json=payload
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ NFT Minting Test Successful!")
            print(f"NFT ID: {response.json().get('id')}")
            return True
        else:
            print("❌ NFT Minting Failed")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request Error: {e}")
        return False

# Run the test
if __name__ == "__main__":
    test_nft_minting()