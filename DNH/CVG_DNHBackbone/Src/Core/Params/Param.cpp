#include "Param.h"

namespace CVG {

	Param::Param(
		const std::string & id, 
		const std::string & label, 
		const std::string & category, 
		const std::string & unit,
		DataType type)
	{
		this->id		=	id;
		this->label		=	label;
		this->category	=	category;
		this->unit		=   unit;
		this->type		=	type;
	}

	bool Param::IsJSONType(const std::string& ty) const
	{
		return this->GetJSONType() == ty;
	}

	std::string Param::GetJSONType() const
	{
		return ConvertToString(this->type);
	}

	json Param::GetJSON()
	{
		json ret;

		ret["id"] = this->id;
		if(this->label.size() > 0)
			ret["label"] = this->label;

		ret["type"] = ConvertToString(this->type);

		if (this->category.size() > 0)
			ret["category"] = this->category;

		if (this->unit.size() > 0)
			ret["unit"] = this->unit;

		this->ModifyJSONImpl(ret);

		return ret;
	}

	bool Param::SetValue(const json& value, ValTy ty)
	{
		if (value.is_boolean())
			return this->SetValue((bool)value, ty);
		else if (value.is_number_float())
			return this->SetValue((float)value, ty);
		else if (value.is_number_integer())
			return this->SetValue((int)value, ty);
		else if (value.is_string())
			return this->SetValue((std::string)value, ty);

		return false;
	}

	json Param::GetValueJSON()
	{
		switch (this->type)
		{
		case DataType::Bool:
			{
				bool bv;
				this->GetValue(bv, ValTy::Current);
				return bv;
			}
			break;

		case DataType::Int:
			{
				int iv;
				this->GetValue(iv, ValTy::Current);
				return iv;
			}	
			break;

		case DataType::Float:
			{
				float fv;
				this->GetValue(fv, ValTy::Current);
				return fv;
			}
			break;

		case DataType::Enum:
		case DataType::String:
			{
				std::string sv;
				this->GetValue(sv, ValTy::Current);
				return sv;
			}
			break;
		}

		return nullptr;
	}
}