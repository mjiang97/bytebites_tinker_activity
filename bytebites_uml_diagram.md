# ByteBites UML Class Diagram

```
┌─────────────────────────────────┐
│         Customer                │
├─────────────────────────────────┤
│ - name: String                  │
│ - purchaseHistory: Order[]      │
├─────────────────────────────────┤
│ + getName(): String             │
│ + getPurchaseHistory(): Order[] │
│ + addPurchase(order): void      │
│ + isValidUser(): Boolean        │
└─────────────────────────────────┘
          ▲
          │ has
          │ 1..∞
          │
┌─────────────────────────────────┐
│          Order                  │
├─────────────────────────────────┤
│ - customer: Customer            │
│ - items: MenuItem[]             │
│ - orderDate: DateTime           │
├─────────────────────────────────┤
│ + addItem(item): void           │
│ + removeItem(item): void        │
│ + getItems(): MenuItem[]        │
│ + getTotalCost(): Float         │
│ + getOrderDate(): DateTime      │
│ + getCustomer(): Customer       │
└─────────────────────────────────┘
          ▲
          │ contains
          │ ∞..∞
          │
┌─────────────────────────────────┐
│        MenuItem                 │
├─────────────────────────────────┤
│ - name: String                  │
│ - price: Float                  │
│ - category: String              │
│ - popularityRating: Float       │
├─────────────────────────────────┤
│ + getName(): String             │
│ + getPrice(): Float             │
│ + getCategory(): String         │
│ + getPopularityRating(): Float  │
│ + setPopularityRating(r): void  │
└─────────────────────────────────┘
          ▲
          │ manages
          │ 1..∞
          │
┌─────────────────────────────────┐
│          Menu                   │
├─────────────────────────────────┤
│ - items: MenuItem[]             │
├─────────────────────────────────┤
│ + addItem(item): void           │
│ + removeItem(item): void        │
│ + getItems(): MenuItem[]        │
│ + getItemsByCategory(cat): M[]  │
│ + searchItem(name): MenuItem    │
└─────────────────────────────────┘
```

## Relationships Summary

- **Customer → Order** (1 to many): Each customer has multiple orders in their purchase history
- **Order → MenuItem** (many to many): Each order contains multiple items, and items can appear in multiple orders
- **Menu → MenuItem** (1 to many): A menu manages a collection of menu items

## Key Design Points

- **Attributes** use dashes (-) to indicate private access
- **Methods** use plus (+) to indicate public access
- **Multiplicity** shows relationship cardinality (1 = one, ∞ = many)
- All classes follow beginner-friendly single responsibility principles
