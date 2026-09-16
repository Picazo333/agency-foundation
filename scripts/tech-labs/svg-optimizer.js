/**
 * Neutral Technical Foundation - SVG Optimizer & Sanitizer Proof-of-Concept
 *
 * Demonstrates the required pipeline for SVGs before production adoption:
 * 1. Validation (checking for malicious tags like <script>)
 * 2. Sanitization (removing inline event handlers like onclick)
 * 3. Optimization (conceptual wrapper for SVGO)
 */

const fs = require('fs');
const path = require('path');

function validateAndSanitizeSVG(svgContent) {
    console.log('--- Starting SVG Validation & Sanitization ---');
    let sanitizedContent = svgContent;
    let isValid = true;

    // 1. Validation: Check for script tags
    if (sanitizedContent.includes('<script')) {
        console.warn('⚠️ WARNING: <script> tag detected. Rejecting or stripping...');
        sanitizedContent = sanitizedContent.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
        isValid = false;
    }

    // 2. Sanitization: Remove inline event handlers (e.g., onclick, onmouseover)
    const onEventRegex = /\s(on[a-z]+)="[^"]*"/gi;
    if (onEventRegex.test(sanitizedContent)) {
        console.warn('⚠️ WARNING: Inline event handlers detected. Stripping...');
        sanitizedContent = sanitizedContent.replace(onEventRegex, '');
        isValid = false;
    }

    // 3. Optimization (Conceptual - would use svgo in real implementation)
    // Here we just strip basic comments for the POC
    console.log('--- Optimizing SVG (Stripping comments) ---');
    sanitizedContent = sanitizedContent.replace(/<!--[\s\S]*?-->/g, '');

    return {
        isValidOriginal: isValid,
        content: sanitizedContent.trim()
    };
}

// Run the test
const samplePath = path.join(__dirname, '../../labs/svg/sample-unoptimized.svg');
if (fs.existsSync(samplePath)) {
    const originalContent = fs.readFileSync(samplePath, 'utf8');
    console.log('Original SVG:\n', originalContent, '\n');

    const result = validateAndSanitizeSVG(originalContent);
    console.log('\nProcessed SVG:\n', result.content);

    if (!result.isValidOriginal) {
        console.log('\n❌ Original SVG was invalid/unsafe. Sanitized version generated.');
    } else {
        console.log('\n✅ SVG passed validation.');
    }
} else {
    console.error('Sample SVG not found at:', samplePath);
}
