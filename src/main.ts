
import { registerSheetElements } from "pure-web-bottom-sheet";

export function setupBottomSheet() {
	registerSheetElements()
}

var bottomSheetContent: HTMLElement

export function setbottomSheet(content: string) {
	bottomSheetContent.innerHTML = `<!-- Snap points -->
		<div slot="snap" style="--snap: 75%" class="top"></div>
		<div slot="snap" style="--snap: 50%"></div>
		<div slot="snap" style="--snap: 25%" class="initial"></div>
		${content}
		`
}

// @ts-expect-error  // Doesn't like setting attribute on L
L.setupBottomSheet = setupBottomSheet;

// @ts-expect-error  // Doesn't like setting attribute on L
L.setbottomSheet = setbottomSheet;
