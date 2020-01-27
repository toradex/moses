using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace TorizonAppDeploymentAPI
{
    public interface IObjectsCollectionInstantiator<TObject,TModel>
    {
        TObject NewObjectFromModel(TModel model);    
    }

    public interface IObjectsCollectionItem<T>
    {
        void Update(T model);
    }

    /// <summary>
    /// This class keeps a sorted collection of objects, using a key property to sort them 
    /// and providing notifications to 
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class ObjectsCollection<TObject,TModel> : ObservableCollection<TObject> where TObject : class, IObjectsCollectionItem<TModel>
    {
        /// <summary>
        /// Property that should be used as key
        /// </summary>
        private string keyProp;

        /// <summary>
        /// Sorted list of keys
        /// </summary>
        List<IComparable> keys;

        /// <summary>
        /// Object used to instantiate a TObject from a TModel
        /// </summary>
        IObjectsCollectionInstantiator<TObject, TModel> instantiator;

        public ObjectsCollection(string keyProp, IObjectsCollectionInstantiator<TObject,TModel> instantiator)
        {
            this.instantiator = instantiator;
            this.keys = new List<IComparable>();
            this.keyProp = keyProp;
        }

        public void Update(List<TModel> list)
        {
            // list used to store keys, it is compared with current list at the end to remove objects
            List<IComparable> existingkeys = new List<IComparable>();

            foreach (TModel model in list)
            {
                IComparable key = typeof(TModel).GetProperty(keyProp).GetValue(model) as IComparable;
                int index = keys.IndexOf(key);

                if (index == -1)
                {
                    AddObject(model);
                }
                else
                {
                    this[index].Update(model);
                }

                existingkeys.Add(key);
            }

            bool changed = true;

            while (changed)
            {
                changed = false;

                foreach (IComparable key in this.keys)
                {
                    if (!existingkeys.Contains(key))
                    {
                        this.RemoveObject(key);
                        changed = true;
                        break;
                    }
                }
            }
        }       

        public virtual TObject GetObject(IComparable key)
        {
            if (!keys.Contains(key))
                return default(TObject);

            return this[keys.IndexOf(key)];
        }

        public virtual void AddObject(TModel model,bool allocate=true)
        {
            IComparable key = typeof(TModel).GetProperty(keyProp).GetValue(model) as IComparable;
            TObject obj;

            if (allocate)
                obj = instantiator.NewObjectFromModel(model);
            else
                obj = model as TObject;

            if (obj == null)
                return;
          
            // add the new key and sort the list
            this.keys.Add(key);
            this.keys.Sort();

            int index = this.keys.IndexOf(key);

            this.Insert(index, obj);
        }

        public virtual void RemoveObject(IComparable key)
        {
            int index = this.keys.IndexOf(key);

            this.keys.Remove(key);
            this.RemoveAt(index);
        }
    }
}
