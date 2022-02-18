#include "Tile.h"

Tile::Tile(DashboardGrid * gridOwner, const std::string& eqGuid)
{
	this->gridOwner = gridOwner;
	this->guid = eqGuid;
}

void Tile::SetLabel(const std::string& newLabel)
{
	if(newLabel.empty())
		this->label = this->DefaultLabel();
	else
		this->label = newLabel;
}

bool Tile::CellInTile(const wxPoint& cell)
{
	if(cell.x < this->gridPos.x)
		return false;

	if(cell.y < this->gridPos.y)
		return false;

	if(cell.x >= this->gridPos.x + this->gridSize.x)
		return false;

	if(cell.y >= this->gridPos.y + this->gridSize.y)
		return false;

	return true;
}


Tile::~Tile()
{}