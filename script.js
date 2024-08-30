const emojiBox = document.querySelector('.emoji-box');
const folderUrl = 'svg/';

const svgFiles = [
  'happy_face.svg'
];

svgFiles.forEach(file => {
  const svgUrl = folderUrl + file;
  
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
});