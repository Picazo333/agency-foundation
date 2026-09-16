/**
 * Neutral Technical Foundation — SVG inspection proof of concept.
 *
 * SECURITY BOUNDARY:
 * This script is intentionally NOT a production sanitizer. Regex-based removal
 * cannot make arbitrary SVG/XML safe. It only demonstrates detection/removal of
 * the specific lab fixtures below so the future pipeline can be reasoned about.
 *
 * Production requirement:
 * untrusted SVG -> vetted parser/sanitizer + explicit allowlist/policy ->
 * adversarial tests/security review -> optimization -> component conversion.
 */

const fs = require('fs');
const path = require('path');

function inspectFixture(svgContent) {
    console.log('--- SVG lab fixture inspection ---');
    let processedContent = svgContent;
    const findings = [];

    // Demonstration fixture 1: <script> blocks.
    const scriptRegex = /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi;
    if (scriptRegex.test(processedContent)) {
        findings.push('script-tag');
        processedContent = processedContent.replace(scriptRegex, '');
    }

    // Demonstration fixture 2: double-quoted inline event handlers.
    // This intentionally does NOT claim coverage of every SVG/XML event syntax.
    const onEventRegex = /\s(on[a-z]+)="[^"]*"/gi;
    if (onEventRegex.test(processedContent)) {
        findings.push('inline-event-handler');
        processedContent = processedContent.replace(onEventRegex, '');
    }

    // Demonstration-only cleanup, not real optimization.
    processedContent = processedContent.replace(/<!--[\s\S]*?-->/g, '');

    return {
        findings,
        demoOutput: processedContent.trim()
    };
}

const samplePath = path.join(__dirname, '../../labs/svg/sample-unoptimized.svg');

if (!fs.existsSync(samplePath)) {
    console.error('Sample SVG not found at:', samplePath);
    process.exitCode = 1;
} else {
    const originalContent = fs.readFileSync(samplePath, 'utf8');
    const result = inspectFixture(originalContent);

    console.log('Findings:', result.findings.length ? result.findings.join(', ') : 'none in demo rules');
    console.log('\nDemo output:\n', result.demoOutput);
    console.log(
        '\nNOTE: This output is NOT production-safe merely because the known demo fixtures were removed.'
    );
}
