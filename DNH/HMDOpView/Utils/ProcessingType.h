#pragma once
#include <string>
/// <summary>
/// enum for types of processing to apply
/// </summary>
enum class ProcessingTypeEnum {
	/// <summary>
	/// no processing needs to be applied
	/// </summary>
	None,

	/// <summary>
	/// apply yen thresholding with all the bells and whistles around it
	/// </summary>
	yen_threshold,

	/// <summary>
	/// apply yen thresholding in a compressed fashion, no dialation, no floodfill
	/// </summary>
	yen_threshold_compressed,
	
	/// <summary>
	/// apply a simple threshold 2 standard deviations away from the mean
	/// </summary>
	two_stdev_from_mean,

	/// <summary>
	/// This threshold is a static number defined by the user
	/// </summary>
	static_threshold,

	/// <summary>
	/// not implemented
	/// </summary>

};

class ProcessingType {
	private:
		ProcessingTypeEnum type;
		int value; // only needs to be initialised in case of static threshold	

	public :
		ProcessingType(ProcessingTypeEnum type, int value)
		{
			this->type = type;
			this->value = value;
		};

		ProcessingTypeEnum getType()
		{return type;}
		
		int getValue()
		{return value;}
};


/// <summary>
/// Convert a ProcessingType to a serialiable string value.
/// 
/// The name convention is made to match std::to_string() functions.
/// </summary>
/// <param name="ty">The ProcessingType to get the name of.</param>
/// <returns>
/// A serializable string version of ProcessingType that can be converted
/// back with ProcessingType().
/// </returns>
std::string to_string(ProcessingType ty);

/// <summary>
/// Convert a serialiable string value to a ProcessingType.
/// </summary>
/// <param name="str">TThe name of a ProcessingType to convert to a Processing Type.</param>
/// <returns>
/// The correct ProcessingType as defined by the ProcessingType string. If the string is not recognized,
/// it is defaulted to ProcessingType::None.
/// </returns>
ProcessingType StringToProcessingType(const std::string& str);

/// <summary>
/// Convert a serialiable float value to a ProcessingType.
/// </summary>
/// <param name="value">The value of a static threshold.</param>
/// <returns>
/// A static_threshold ProcessingType with the value given. 
/// </returns>
ProcessingType IntToProcessingType(int value);