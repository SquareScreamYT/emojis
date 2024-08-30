const emojiBox = document.querySelector('.emoji-box');
const folderUrl = 'svg/';

function loadSvgFiles() {
  fetch(folderUrl)
    .then(response => response.text())
    .then(data => {
      const parser = new DOMParser();
      const htmlDoc = parser.parseFromString(data, 'text/html');
      const links = htmlDoc.querySelectorAll('a');
      
      links.forEach(link => {
        const fileName = link.getAttribute('href');
        if (fileName.endsWith('.svg')) {
          createEmojiButton(fileName);
        }
      });
    })
    .catch(error => console.error('Error loading SVG files:', error));
}

function createEmojiButton(fileName) {
  const svgUrl = folderUrl + fileName;
  
  const button = document.createElement('button');
  button.className = 'emoji-button';
  button.innerHTML = `<img src="${svgUrl}" alt="Emoji" width="32" height="32">`;
  
  button.addEventListener('click', () => {
    const embedLink = `https://sq.is-a.dev/emojis/${svgUrl}`;
    navigator.clipboard.writeText(embedLink)
      .then(() => {
        alert('Embed link copied to clipboard!');
      })
      .catch(err => {
        console.error('Failed to copy: ', err);
      });
  });

  emojiBox.appendChild(button);
}

loadSvgFiles();
