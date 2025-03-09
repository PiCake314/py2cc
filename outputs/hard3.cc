#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;


auto greet(const auto& name) {
	std::println("{} {}", "Hello,"s, name);
}



int main()
{
	greet("Ali"s);
}


