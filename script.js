const facesBox = document.getElementById('faces');
const foodBox = document.getElementById('food');
const folderUrl = 'svg/';
const repoOwner = 'SquareScreamYT';
const repoName = 'emojis';

function loadSvgFiles() {
  const folders = ['faces', 'food'];
  
  folders.forEach(folder => {
    fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contents/svg/${folder}`)
      .then(response => response.json())
      .then(data => {
        data.forEach(file => {
          if (file.name.endsWith('.svg')) {
            createEmojiButton(file.name, folder);
          }
        });
      })
      .catch(error => console.error(`Error loading SVG files from ${folder}:`, error));
  });
}

function createEmojiButton(fileName, folder) {
  const svgUrl = `${folderUrl}${folder}/${fileName}`;
  
  const button = document.createElement('button');
  button.className = 'emoji-button';
  button.innerHTML = `<img src="${svgUrl}" alt="${fileName.replace(".svg", "").replace(/_/g, " ")}" width="32" height="32">
  <br><span>${fileName.replace(".svg", "").replace(/_/g, " ")}</span>`;
  
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

  if (folder === 'faces') {
    facesBox.appendChild(button);
  } else if (folder === 'food') {
    foodBox.appendChild(button);
  }
}

loadSvgFiles();
