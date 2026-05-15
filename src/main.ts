import { registerSheetElements } from 'pure-web-bottom-sheet';

export function setupBottomSheet() {
	registerSheetElements();
}

export function setBottomSheetContent(content: string) {
	document.getElementById('bottomSheetContent')!.innerHTML = `<!-- Snap points -->
		<div slot="snap" style="--snap: 75%" class="top"></div>
		<div slot="snap" style="--snap: 50%"></div>
		<div slot="snap" style="--snap: 25%" class="initial"></div>
		${content}
		`;
}

export function getBottomSheetDialog(): HTMLDialogElement | null {
	return document.getElementById('bottomSheetDialog') as (HTMLDialogElement | null);
}

// @ts-expect-error  // Doesn't like setting attribute on L
L.setupBottomSheet = setupBottomSheet;

// @ts-expect-error  // Doesn't like setting attribute on L
L.setBottomSheetContent = setBottomSheetContent;

// @ts-expect-error  // Doesn't like setting attribute on L
L.getBottomSheetDialog = getBottomSheetDialog;
