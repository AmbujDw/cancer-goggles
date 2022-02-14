#pragma once
#include "InsWidgetParam.h"
#include <wx/spinctrl.h>

/// <summary>
/// Default implementation of a InsWidgetParam for int Params.
/// </summary>
class InsWidgetInt : 
	public InsWidgetParam,
	public wxSpinCtrl
{
private:
	bool destroyed = false;

public:

	InsWidgetInt(InspectorParam* owner, CVGBridge* bridge);

	void UpdateDisplay() override;
	void DestroyUI() override;
	wxWindow* GetWindow() override;

	// Event callback when the user presses the "Enter" key in the 
	// text input field.
	void OnTextEnter(wxCommandEvent& evt);

	// Event callback when the input field changes keyboard focus.
	// Specifically when the input field looses keyboard focus.
	void OnFocusChange(wxFocusEvent& evt);

	// Event callback when the text value changes.
	void OnValChanged(wxSpinEvent& evt);

	void OnDestroy(wxWindowDestroyEvent& evt);

	wxDECLARE_EVENT_TABLE();
};