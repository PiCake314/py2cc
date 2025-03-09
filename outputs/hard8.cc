#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <utility>
#include <ranges>

#include <optional>
#include <variant>
#include <any>


using namespace std::literals;



auto func() {
}	// "pass"

auto a() {
	if (true) 
	;	// "pass"
	else 
	;	// "pass"
}

auto b() {
	if (true) if (false) if (1) 
	;	// "pass"
	else 
	;	// "pass"
	else 
	;	// "pass"
	else 
	;	// "pass"
}

auto c() {
	if (true) if (false) if (1) 
	;	// "pass"
	else {
		1;
		2;
	}
	else {
		3;
		4;
	}
	else {
		5;
		6;
	}
}
int main()
{
}


