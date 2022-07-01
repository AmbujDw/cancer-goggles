#include "HMDOpSub_WidgetCtrl.h"
#include "../StateHMDOp.h"

#include "../../UISys/UIHSlider.h"
#include "../../UISys/UIButton.h"

HMDOpSub_WidgetCtrl::HMDOpSub_WidgetCtrl(UIButton* btn)
{
	this->categoryBtn = btn;
}

void HMDOpSub_WidgetCtrl::OnLeftDown(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm) 
{
	UIBase* uiSel = targ.uiSys.GetSelected();
	// Validate and typecast.
	auto it = std::find(this->sliders.begin(), this->sliders.end(), (UIHSlider*)uiSel);
	if(it == this->sliders.end())
		return;

	(*it)->MoveQuantizedAmt(10, -1);
}

void HMDOpSub_WidgetCtrl::OnLeftUp(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
}

void HMDOpSub_WidgetCtrl::HMDOpSub_WidgetCtrl::OnMiddleUp(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
	if(this->sliders.size() <= 1)
		return;

	UIHSlider* uiSel = (UIHSlider*)targ.uiSys.GetSelected();
	if(uiSel == nullptr)
		return;

	auto itFind = std::find(this->sliders.begin(), this->sliders.end(), uiSel);
	if(itFind == this->sliders.end())
	{
		targ.uiSys.Select(sliders[0]);
		return;
	}

	++itFind;
	if(itFind == this->sliders.end())
		targ.uiSys.Select(this->sliders[0]);
	else
		targ.uiSys.Select(*itFind);

}

void HMDOpSub_WidgetCtrl::OnMiddleUpHold(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
	ssm.PopSubstate();
}

void HMDOpSub_WidgetCtrl::OnRightDown(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
	UIBase* uiSel = targ.uiSys.GetSelected();
	// Validate and typecast.
	auto it = std::find(this->sliders.begin(), this->sliders.end(), (UIHSlider*)uiSel);
	if(it == this->sliders.end())
		return;

	(*it)->MoveQuantizedAmt(10, 1);
}

void HMDOpSub_WidgetCtrl::OnRightUp(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
}

void HMDOpSub_WidgetCtrl::OnEnterContext(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm)
{
	auto it = targ.camButtonGrouping.find(this->categoryBtn);
	if(it == targ.camButtonGrouping.end())
		return;

	for(StateHMDOp::PlateSliderPair psp : it->second)
		this->sliders.push_back(psp.slider);

	if(!this->sliders.empty())
		targ.uiSys.Select(this->sliders[0]);
}

void HMDOpSub_WidgetCtrl::OnExitContext(StateHMDOp& targ, SubstateMachine<StateHMDOp>& ssm) 
{
	targ.ManageCamButtonPressed(-1);
	targ.uiSys.Select(this->categoryBtn);
}

std::string HMDOpSub_WidgetCtrl::GetStateName() const
{
	return "WidgetCtrl";
}