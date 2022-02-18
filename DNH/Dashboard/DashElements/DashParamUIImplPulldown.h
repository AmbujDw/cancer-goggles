#pragma once
#include "DashParamUIImpl.h"
#include <wx/choice.h>

/// <summary>
/// Default dashboard UI implementation for enum types.
/// </summary>
class DashParamUIImplPulldown : 
	public DashParamUIImpl,
	public wxChoice
{
public:
	DashParamUIImplPulldown(wxWindow* parent, DashboardElementInst* eleInst);

protected:
	bool Reattach() override;
	std::string ImplName() override;
	void Layout(const wxPoint& pixelPt, const wxSize& pixelSz, int cellSize) override;
	void DestroyWindow() override;
	void OnParamValueChanged() override;
	void DrawPreview(wxPaintDC& dc, const wxPoint& offset) override;
	void Toggle(bool show) override;

	// Event handler for when the user changes the pulldown value.
	void OnChanged(wxCommandEvent& evt);

	DECLARE_EVENT_TABLE();
};