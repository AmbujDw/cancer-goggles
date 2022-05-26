#include "ProcessingType.h"
#include <string>

std::string to_string(ProcessingType ty)
{
	switch (ty.getType())
	{

	case ProcessingTypeEnum::None:
		return "None";

	case ProcessingTypeEnum::yen_threshold:
		return "yen_threshold";

	case ProcessingTypeEnum::yen_threshold_compressed:
		return "yen_threshold_compressed";

	case ProcessingTypeEnum::static_threshold:
		return std::to_string(ty.getValue());
	}

	return "other";//This should never happen, maybe this is a failed assert?
}

ProcessingType StringToProcessingType(const std::string& str)
{
	if (str == "yen_threshold")
		return ProcessingType(ProcessingTypeEnum::yen_threshold,NULL);

	if (str == "yen_threshold_compressed")
		return ProcessingType(ProcessingTypeEnum::yen_threshold_compressed,NULL);

	if (str == "None")
		return ProcessingType(ProcessingTypeEnum::None,NULL);

	/// default to None
	return ProcessingType(ProcessingTypeEnum::None,NULL);
}

ProcessingType IntToProcessingType(int value)
{
	return ProcessingType(ProcessingTypeEnum::static_threshold, value);
}