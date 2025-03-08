#include <stdio.h>

int main()
{
    int foodType = 0, itemNumber = 0;
    puts("Welcome to our restaurant The Taste");
    puts("What you wish to have Veg:1, NonVeg:2. You choice please");
    scanf("%d", &foodType);
    switch (foodType)
    {
    case 1:
        puts("1:DB-Dosa 2:ChowChowBath 3:Idly-Vada 4:BB-Bath. Your choice please: ");
        scanf("%d", &itemNumber);
        switch (itemNumber)
        {
        case 1: puts("Yummy Davanagere Benne Dosa Maam"); break;
        case 2: puts("Spicy kahara bath and tasty Shira"); break;
        case 3: puts("Soft Idli and hot Vada Maam"); break;
        case 4: puts("Fresh Hot bath with Pure Ghee Sir"); break;
        default:puts("Sorry we dont serve your choice of food");
        }
    case 2: puts("1:Fish-Fry 2:Chicken-Biryani 3:Hanumantu-Palav 4:Egg-Masala. Your choice please: ");
        scanf("%d", &itemNumber);
        switch (itemNumber)
        {
        case 1: puts("Tasty fish from Mangalore Maam"); break;
        case 2: puts("Nati Dum Biryani for you Sir!!!"); break;
        case 3: puts("Famous palav for you Maam"); break;
        case 4: puts("Delicious Egg masala Maam!!!"); break;
        default:puts("Sorry we dont serve Lizards and Cockroaches!");
        }
        default:puts("This is Restaurtant, not Garden. Please Order an item");
    }
    puts("Namaste Visit Again");
}