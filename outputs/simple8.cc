#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;





int main()
{
	std::println("{}", true or true or true and true and true and true);
	std::println("{}", false or false and false);
	std::println("{}", true and false or true);
}


