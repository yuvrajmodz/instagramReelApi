import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from flask import Flask, request, redirect, jsonify
import os

app = Flask(__name__)

#╔════════════════════════════╗
#║                                            
#║    𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 © 𝟮𝟬𝟮𝟰 𝗬𝗨𝗩𝗥𝗔𝗝𝗠𝗢𝗗𝗭     
#║     𝗖𝗥𝗘𝗗𝗜𝗧: 𝐌𝐀𝐓𝐑𝐈𝐗 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑      
#║                                           
#╚════════════════════════════╝

async def download_video(url_to_download):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        await page.goto("https://fastvideosave.net")

        await page.fill("input[name='url']", url_to_download)

        await page.click("button[type='submit']")

        await page.wait_for_selector("div.text-center.pt-2.mb-2.-mt-2.text-sm", state="visible")
        await page.wait_for_selector("div.text-center.pt-2.mb-2.-mt-2.text-sm", state="hidden")

        await asyncio.sleep(2)

        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")

        download_link = None
        for link in soup.find_all("a", href=True):
            if "https://dl.fastvideosave.net/?url=" in link['href']:
                download_link = link['href']
                break

        await browser.close()

        return download_link

@app.route('/download', methods=['GET'])
def download_endpoint():
    url_to_download = request.args.get('link')
    if not url_to_download:
        return jsonify({"error": "No link provided"}), 400

    if not url_to_download.startswith("https://www.instagram.com/"):
        return jsonify({"error": "Invalid URL. Only Instagram links are allowed."}), 400

    download_link = asyncio.run(download_video(url_to_download))
    if download_link:
        return redirect(download_link)
    else:
        return jsonify({"error": "Download link not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5016))
    app.run(host='0.0.0.0', port=port, debug=True)