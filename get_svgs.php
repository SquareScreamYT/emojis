<?php
header('Content-Type: application/json');

$svgFolder = 'svg/';
$svgFiles = glob($svgFolder . '*.svg');

$fileNames = array_map(function($file) use ($svgFolder) {
    return str_replace($svgFolder, '', $file);
}, $svgFiles);

echo json_encode($fileNames);