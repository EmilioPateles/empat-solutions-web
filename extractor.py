import asyncio
from playwright.async_api import async_playwright
import requests
import os
from urllib.parse import urljoin, urlparse

# Konfiguracja celu
TARGET_URL = "https://www.empat.me/"
SUBPAGES = [
    TARGET_URL,
    # Tutaj dodaj inne podstrony, np.:
    # "https://www.empat.me/o-mnie",
    # "https://www.empat.me/oferta"
]
OUTPUT_DIR = "exfiltrated_data"
IMG_DIR = os.path.join(OUTPUT_DIR, "images")

# Zabezpieczenie: Tworzenie struktury katalogów
os.makedirs(IMG_DIR, exist_ok=True)

async def scrape_wix_site():
    print("[*] Inicjalizacja silnika Playwright...")
    async with async_playwright() as p:
        # Uruchamiamy przeglądarkę w trybie headless (w tle)
        browser = await p.chromium.launch(headless=True)
        
        # Maskowanie tożsamości bota (OPSEC: User-Agent Spoofing)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        with open(os.path.join(OUTPUT_DIR, "extracted_content.md"), "w", encoding="utf-8") as f:
            for url in SUBPAGES:
                print(f"[*] Rozpoczynam infiltrację celu: {url}")
                try:
                    # Modyfikacja 1: Zmiana strategii oczekiwania i wydłużenie timeoutu do 60s
                    await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                    
                    print("[*] Faza 1: Sztywny DOM załadowany. Omijanie Lazy-Loadingu...")
                    
                    # Modyfikacja 2: Symulacja przewijania strony przez człowieka
                    # Przewijamy stronę w dół w kilku krokach, by wyzwolić skrypty JS ładujące treść
                    for _ in range(6):
                        await page.mouse.wheel(0, 1500)
                        await asyncio.sleep(1.5) # Krótkie pauzy na renderowanie
                    
                    # Dodatkowy bufor na załadowanie wyzwolonych elementów
                    await asyncio.sleep(3)
                    
                    # Ekstrakcja struktury tekstowej
                    f.write(f"\n\n## URL: {url}\n\n")
                    
                    print("[+] Ekstrakcja wektorów tekstowych...")
                    elements = await page.query_selector_all("h1, h2, h3, p, span")
                    for el in elements:
                        text = await el.inner_text()
                        if text and len(text.strip()) > 5:
                            f.write(f"{text.strip()}\n\n")

                    # Ekstrakcja zasobów graficznych
                    print("[+] Rekonesans zasobów graficznych (IMG)...")
                    images = await page.query_selector_all("img")
                    for img in images:
                        src = await img.get_attribute("src")
                        if src and "http" in src:
                            download_image(src)

                except Exception as e:
                    print(f"[!] Błąd krytyczny podczas przetwarzania {url}: {e}")
                
                # Omijanie progów detekcji heurystycznej WAF
                print("[*] Evasion: Oczekiwanie przed kolejnym żądaniem (Low and Slow)...")
                await asyncio.sleep(2)

        await browser.close()
        print("[+] Operacja zakończona sukcesem. Dane zabezpieczone lokalnie.")

def download_image(url):
    try:
        # Czyszczenie URL z parametrów śledzących i formatowania Wix
        clean_url = url.split("?")[0]
        filename = os.path.basename(urlparse(clean_url).path)
        
        # Zabezpieczenie przed nadpisywaniem i błędnymi nazwami
        if not filename or len(filename) > 50:
            filename = f"asset_{hash(url)}.jpg"
            
        filepath = os.path.join(IMG_DIR, filename)
        
        if not os.path.exists(filepath):
            response = requests.get(url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"  [+] Zabezpieczono plik: {filename}")
    except Exception as e:
        print(f"  [-] Ostrzeżenie: Nie udało się pobrać zasobu {url}. Powód: {e}")

if __name__ == "__main__":
    asyncio.run(scrape_wix_site())

