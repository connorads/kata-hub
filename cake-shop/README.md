# Cake Shop Kata

Cake Delights is an artisan cake shop that specializes in custom-made cakes for delivery. The cake shop is owned by two friends, Edward and Arthur.

Edward and Arthur are eager to expand their business by selling cakes online. They need your help in developing a code that can calculate the delivery date for their cakes.

## Why this Kata?

In software development, seemingly simple requirements can become complicated due to their interactions. The goal is to work through the requirements step by step, refactoring the code as needed to keep the solution simple and easy to understand.

## Requirements

Cake Delights is an artisan bakery that offers custom-made cakes for delivery. The cake shop is owned by two friends, Edward and Arthur. Edward handles the baking, while Arthur takes care of the decorations.

Edward and Arthur want to enable online cake orders and require a code that can determine the delivery date for each cake. Here are the specific requirements:

* Edward works from Monday to Friday, and Arthur works from Tuesday to Saturday.
* The "lead time" refers to the number of days required to make a cake.
* Cakes are always delivered on the day they are completed to ensure freshness.
* Small cakes have a lead time of 2 days.
* Big cakes have a lead time of 3 days.
* If Edward receives a cake order in the morning (before 12pm), he starts working on it on the same day.
* Adding custom frosting to a cake extends the lead time by 2 days. Frosting can only be applied after the cake is baked.
* The shop offers fancy boxes for gift-wrapping cakes. Fancy boxes require an additional lead time of 3 days. These boxes can arrive while Edward and Arthur are working on the cake.
* Decorating cakes with nuts is done by Edward since Arthur is allergic. This process takes 1 extra day and must occur after the frosting is applied.
* The shop closes for Christmas from the 23rd of December and reopens on the 2nd of January. Any cakes that would be completed during this period cannot start production until the shop reopens. However, fancy boxes can still arrive during the festive period.

## Examples

The delivery date for a cake is determined by adding the lead time to the order date.

* An order for a cake placed on the 1st of the month, with a 2-day lead time, will be delivered on the 3rd of the month.

Small cakes have a lead time of 2 days:

* An order for a small cake placed on Monday afternoon will be delivered on Wednesday.

Big cakes have a lead time of 3 days:

* An order for a big cake placed on Monday afternoon will be delivered on Thursday.

If a cake order is received in the morning (before 12pm), baking starts on the same day:

* An order for a small cake placed on Monday morning will be delivered on Tuesday.

Custom frosting adds 2 days to the lead time. Frosting can only be applied after the cake is baked:

* An order for a small cake with custom frosting placed on Monday morning will be delivered on Thursday.
  * Edward bakes the cake on Monday and Tuesday.
  * Arthur applies the frosting on Wednesday and Thursday.

Edward only works from Monday to Friday:

* An order for a small cake received on Friday morning will be delivered on Monday.
* An order for a small cake with frosting received on Friday morning will be delivered on Wednesday.

Arthur works from Tuesday to Saturday:

* An order for a big cake with custom frosting received on Tuesday afternoon will be delivered on Tuesday.
  * Edward bakes the cake on Wednesday, Thursday, and Friday.
  * Arthur applies the frosting on Saturday and Tuesday.

Fancy boxes require a lead time of

 3 days. They can be ordered from the supplier before the cakes are finished:

* An order for a small cake with a fancy box placed on Monday morning will be delivered on Wednesday.
  * Edward bakes the cake on Monday and Tuesday.
  * The box arrives on Wednesday.
* An order for a big cake with a fancy box placed on Monday morning will be delivered on Wednesday.
  * Edward bakes the cake from Monday to Wednesday.
  * The box arrives on Wednesday.
* An order for a big cake with a fancy box placed on Monday afternoon will be delivered on Thursday.
  * Edward bakes the cake from Tuesday to Thursday.
  * The box arrives on Wednesday.

Since Arthur is allergic to nuts, adding nuts to a cake is done by Edward. This process takes 1 day and must occur after the frosting is applied:

* An order for a small cake with nuts placed on Monday morning will be delivered on Wednesday.
  * Edward bakes the cake on Monday and Tuesday.
  * Edward adds nuts on Wednesday.
* An order for a small cake with frosting placed on Monday morning will be delivered on Friday.
  * Edward bakes the cake on Monday and Tuesday.
  * Arthur applies the frosting on Wednesday and Thursday.
  * Edward adds nuts on Friday.
* An order for a small cake with frosting, in a fancy box, placed on Tuesday morning will be delivered on Monday.
  * Edward bakes the cake on Tuesday and Wednesday.
  * Arthur applies the frosting on Thursday and Friday.
  * The box arrives on Friday.
  * Edward adds nuts on Monday.

The shop closes for Christmas from the 23rd of December and reopens on the 2nd of January. Cakes that would be completed during this period cannot start production until the shop reopens:

* A small cake ordered on the 22nd of December will be delivered on the 3rd of January.
  * Edward bakes the cake on the 2nd and 3rd of January.
* A small cake ordered on the 22nd of December 2021 will be delivered on the 4th of January.
  * The shop normally reopens on the 2nd of January, but as it falls on a Sunday, Edward starts baking the cake on Monday, the 3rd.
* A small cake ordered on the morning of the 21st of December will be delivered on the 22nd of December.

Fancy boxes can still arrive during the festive period:

* A small cake with a fancy box ordered on the 22nd of December will be delivered on the 3rd of January.
  * Edward returns from the holiday on the 2nd of January and bakes the cake.
  * The box arrives on the 25th of December.
* A small cake with a fancy box ordered on the 21st of December will be delivered on the 3rd of January.
  * Edward could bake the cake on the 21st and 22nd, but the box won't arrive until the 23rd.
  * Instead, Edward waits until the 2nd of January to start the cake.

## Credits

This is just the [Cake Shop Kata](https://github.com/bobthemighty/cake-shop-kata) by Bob Gregory paraphrased by an LLM.
