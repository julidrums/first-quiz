package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private int moneyInserted;
    private Map<String, Drink> drinks;

    public VendingMachineImpl() {
        moneyInserted = 0;
        drinks = new HashMap<>();

        // Add drinks 
        drinks.put("ScottCola", new Drink() {
            @Override
            public String getName() {
                return "ScottCola";
            }

            @Override
            public boolean isFizzy() {
                return true;
            }
        });
        drinks.put("KarenTea", new Drink() {
            @Override
            public String getName() {
                return "KarenTea";
            }

            @Override
            public boolean isFizzy() {
                return false;
            }
        });
    }

    @Override
    public void insertQuarter() {
        moneyInserted += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        // Check if the drink is available.
        if (!drinks.containsKey(name)) {
            throw new UnknownDrinkException();
        }

        // Check if enough money has been inserted.
        Drink drink = drinks.get(name);
        int drinkPrice = drink.isFizzy() ? 75 : 100;
        if (moneyInserted < drinkPrice) {
            throw new NotEnoughMoneyException();
        }

        // Dispense the drink and reset the money inserted.
        moneyInserted -= drinkPrice;
        return drink;
    }

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }
}
